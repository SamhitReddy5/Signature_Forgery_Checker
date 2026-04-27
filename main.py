import os
import random
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from sklearn.model_selection import train_test_split

IMG_SIZE = (112, 112)
EPOCHS = 12
BATCH_SIZE = 16
MODEL_PATH = "siamese_signature_model.keras"
TRAIN_DIR = "data/train"


def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    img = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, IMG_SIZE)
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=-1)

    return img


def get_writer_groups(base_dir):
    groups = {}

    for folder in os.listdir(base_dir):
        path = os.path.join(base_dir, folder)

        if os.path.isdir(path):
            groups[folder] = [
                os.path.join(path, f)
                for f in os.listdir(path)
                if f.lower().endswith(("png", "jpg", "jpeg"))
            ]

    return groups


def create_balanced_pairs(base_dir, max_pairs_per_writer=40):
    groups = get_writer_groups(base_dir)
    genuine_writers = [g for g in groups if not g.endswith("_forg")]

    left, right, labels = [], [], []

    for writer in genuine_writers:
        genuine = groups.get(writer, [])
        forged = groups.get(f"{writer}_forg", [])

        if len(genuine) < 2:
            continue

        other_writers = [w for w in genuine_writers if w != writer]
        if not other_writers:
            continue

        # positive pairs
        for _ in range(max_pairs_per_writer):
            a, b = random.sample(genuine, 2)
            left.append(preprocess_image(a))
            right.append(preprocess_image(b))
            labels.append(1)

        # forged negatives
        if forged:
            for _ in range(max_pairs_per_writer):
                a = random.choice(genuine)
                b = random.choice(forged)
                left.append(preprocess_image(a))
                right.append(preprocess_image(b))
                labels.append(0)

        # different writer negatives
        for _ in range(max_pairs_per_writer):
            other_writer = random.choice(other_writers)
            other_genuine = groups.get(other_writer, [])

            if not other_genuine:
                continue

            a = random.choice(genuine)
            b = random.choice(other_genuine)

            left.append(preprocess_image(a))
            right.append(preprocess_image(b))
            labels.append(0)

    return np.array(left), np.array(right), np.array(labels)


def build_embedding_network():
    inp = layers.Input(shape=(112, 112, 1))

    x = layers.Conv2D(32, 3, activation="relu")(inp)
    x = layers.MaxPooling2D()(x)

    x = layers.Conv2D(64, 3, activation="relu")(x)
    x = layers.MaxPooling2D()(x)

    x = layers.Conv2D(128, 3, activation="relu")(x)
    x = layers.MaxPooling2D()(x)

    x = layers.Flatten()(x)
    x = layers.Dense(384, activation="relu")(x)
    x = layers.Dropout(0.35)(x)

    out = layers.Dense(96, activation="relu")(x)

    return Model(inp, out)


def abs_diff(vectors):
    x, y = vectors
    return tf.abs(x - y)


def build_siamese_model():
    base = build_embedding_network()

    inp_a = layers.Input(shape=(112, 112, 1))
    inp_b = layers.Input(shape=(112, 112, 1))

    feat_a = base(inp_a)
    feat_b = base(inp_b)

    diff = layers.Lambda(abs_diff)([feat_a, feat_b])

    x = layers.Dense(64, activation="relu")(diff)
    x = layers.Dropout(0.25)(x)
    out = layers.Dense(1, activation="sigmoid")(x)

    model = Model([inp_a, inp_b], out)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(2e-4),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model


def train():
    print("Creating medium-strength balanced pairs...")
    X1, X2, y = create_balanced_pairs(TRAIN_DIR)

    print(f"Pairs: {len(y)}")
    print(f"Genuine: {np.sum(y==1)}")
    print(f"Forged: {np.sum(y==0)}")

    X1_train, X1_val, X2_train, X2_val, y_train, y_val = train_test_split(
        X1, X2, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = build_siamese_model()

    history = model.fit(
        [X1_train, X2_train],
        y_train,
        validation_data=([X1_val, X2_val], y_val),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )

    model.save(MODEL_PATH)

    print(f"\nModel saved as {MODEL_PATH}")
    print(f"Validation Accuracy: {history.history['val_accuracy'][-1]*100:.2f}%")


if __name__ == "__main__":
    train()