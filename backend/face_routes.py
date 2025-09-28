from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np, io

face_routes = Blueprint("face_routes", __name__)
model = load_model('C:/Project/Bismillahya/face/p.h5')

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((256, 256))
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

@face_routes.route("/analyze-face", methods=["POST"])
def analyze_face():
    if "faceImage" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["faceImage"]
    input_data = preprocess_image(file.read())
    prediction = model.predict(input_data)[0][0]

    label = "Normal" if prediction > 0.01 else "Autisme"
    return jsonify({"result": label, "confidence": float(prediction)})
