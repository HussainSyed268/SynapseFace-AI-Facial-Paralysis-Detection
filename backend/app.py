from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.model import process_image
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

    # Convert the image to a format OpenCV can understand
        in_memory_file = io.BytesIO()
        image_file.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1  # Use 0 for grayscale
        image = cv2.imdecode(data, color_image_flag)



        # image_buffer = BytesIO()
        # image.save(image_buffer)
        # image_buffer.seek(0)
        # pil_image = Image.open(image_buffer)
        # pil_image = pil_image.convert('RGB')
        # output = process_image(pil_image)
        output = process_image(image)


        result_image = output[0]
        result_string = output[1]

        # Return the result to the frontend
        # return jsonify({'result_image': result_image, 'result_string': result_string})
        return jsonify({"msg": "hello"})

if __name__ == '__main__':
        app.run()
