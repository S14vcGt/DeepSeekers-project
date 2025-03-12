from flask import Flask, request, jsonify
from flask_cors import CORS
import model
import os

app = Flask(__name__)
CORS(app)

@app.route('/answer', methods=['POST'])
def answer():

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    result = model.predict_plant(file_path)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
