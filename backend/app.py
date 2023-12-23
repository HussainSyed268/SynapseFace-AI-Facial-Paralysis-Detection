from flask import Flask, request, jsonify
from flask_cors import CORS
from model import process_image
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)
@app.route('/process_image', methods=['POST'])

def process_image_route():
        # Get the uploaded image from the frontend
        print("image received by app")
        image = request.files['image']
        
        print("app.py got image")

        # Save the file content to a BytesIO buffer
        image_buffer = BytesIO()
        image.save(image_buffer)
        image_buffer.seek(0)

        # Open the image using PIL (Python Imaging Library)
        pil_image = Image.open(image_buffer)

        # Convert the image to JPG format (you can also specify other formats)
        pil_image = pil_image.convert('RGB')

        # Pass the image to the model for processing (defined in model.py?)
        output = process_image(pil_image)
        result_image = output[0]
        result_string = output[1]

        # Return the result to the frontend
        # return jsonify({'result_image': result_image, 'result_string': result_string})
        return jsonify({"msg": "hello"})

if __name__ == '__main__':
        app.run()
