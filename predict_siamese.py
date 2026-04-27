import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = "siamese_signature_model.keras"
IMG_SIZE = (112, 112)
THRESHOLD = 0.68


def abs_diff(vectors):
    x, y = vectors
    return tf.abs(x - y)


model = tf.keras.models.load_model(
    MODEL_PATH,
    custom_objects={"abs_diff": abs_diff},
    safe_mode=False
)


def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError(f"Could not read image: {path}")

    img = cv2.threshold(
        img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    img = cv2.GaussianBlur(img, (3, 3), 0)

    img = cv2.resize(img, IMG_SIZE)

    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=(0, -1))

    return img


def verify_signature(img1_path, img2_path):
    img1 = preprocess_image(img1_path)
    img2 = preprocess_image(img2_path)

    score = float(model.predict([img1, img2], verbose=0)[0][0])

    label = "Genuine" if score >= THRESHOLD else "Forged"

    confidence = (
        score * 100
        if label == "Genuine"
        else (1 - score) * 100
    )

    return {
        "label": label,
        "score": round(score, 4),
        "confidence": round(confidence, 2)
    }