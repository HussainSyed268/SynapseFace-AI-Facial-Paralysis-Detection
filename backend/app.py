from flask import Flask, request, jsonify
from model import process_image

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])

def process_image_route():
        # Get the uploaded image from the frontend
        image = request.files['image']

        # Pass the image to the model for processing (defined in model.py?)
        result_image, result_string = process_image(image)

        # Return the result to the frontend
        return jsonify({'result_image': result_image, 'result_string': result_string})

if __name__ == '__main__':
        app.run()
