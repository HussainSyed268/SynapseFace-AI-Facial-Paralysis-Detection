from flask import Flask, request, jsonify
from flask_cors import CORS
from model import process_image
import numpy as np
from PIL import Image
import io
import cv2
import base64

app = Flask(__name__)
CORS(app)

@app.route('/process_image', methods=['POST'])
def process_image_route():
    if 'image' not in request.files:
        return jsonify({'message': 'No image part in the request'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'message': 'No image selected for uploading'}), 400

    if file:
        in_memory_file = io.BytesIO()
        file.save(in_memory_file)
        data = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        image = cv2.imdecode(data, color_image_flag)

        output = process_image(image)
        result_image = output[0]
        result_string = output[1]

        # Encode the image to a base64 string
        _, buffer = cv2.imencode('.jpg', result_image)
        base64_image = base64.b64encode(buffer).decode('utf-8')

        # Determine the message to send based on result_string
        message = "Facial paralysis detected" if result_string == 1.0 else "Facial paralysis not detected"

        return jsonify({'image': base64_image, 'message': message}), 200

    else:
        return jsonify({'message': 'Allowed image types are -> png, jpg, jpeg, gif'}), 400

if __name__ == '__main__':
    app.run(port=5001)
