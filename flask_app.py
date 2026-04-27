from flask import Flask, render_template, request
import os
from predict_siamese import verify_signature

app = Flask(__name__, template_folder="templates")
UPLOAD_DIR = "flagged"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        ref_file = request.files["reference"]
        test_file = request.files["test"]

        ref_path = os.path.join(UPLOAD_DIR, "reference.png")
        test_path = os.path.join(UPLOAD_DIR, "test.png")

        ref_file.save(ref_path)
        test_file.save(test_path)

        result = verify_signature(ref_path, test_path)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)