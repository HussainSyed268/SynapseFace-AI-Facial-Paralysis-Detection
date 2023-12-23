from flask import Flask, request, jsonify
from flask_cors import CORS
from model import process_image

app = Flask(__name__)
CORS(app)
@app.route('/process_image', methods=['POST'])

def process_image_route():
        # Get the uploaded image from the frontend
        image = request.files['image']

        # Pass the image to the model for processing (defined in model.py?)
        output = process_image(image)
        result_image = output[0]
        result_string = output[1]

        # Return the result to the frontend
        return jsonify({'result_image': result_image, 'result_string': result_string})

if __name__ == '__main__':
        app.run()
