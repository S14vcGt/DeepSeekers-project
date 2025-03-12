from flask import Flask, request, jsonify
from flask_cors import CORS
from env_script import download_model
import model
import os

download_model()
uploads='uploads'
os.makedirs(uploads, exist_ok=True)
print(f"Carpeta '{uploads}' creada exitosamente.")

app = Flask(__name__)
CORS(app)


@app.route('/api/predict', methods=['POST'])
def predict():

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(uploads, file.filename)
    file.save(file_path)

    result: dict = model.predict_plant(file_path)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
