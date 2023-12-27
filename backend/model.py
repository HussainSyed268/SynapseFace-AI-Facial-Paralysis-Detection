import joblib
import numpy as np
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor_path = 'shape_predictor_68_face_landmarks.dat'  # Replace with the actual path
# predictor_path = 'backend\shape_predictor_68_face_landmarks.dat'  # Replace with the actual path
predictor = dlib.shape_predictor(predictor_path)

def calculate_angle(point1, point2, point3):
    vector1 = point1 - point2
    vector3 = point3 - point2
    dot_product = np.dot(vector1, vector3)
    norm_product = np.linalg.norm(vector1) * np.linalg.norm(vector3)

    # Check for almost zero division to avoid invalid values
    if np.isclose(norm_product, 0.0):
        return 0.0  # or any default value you prefer

    angle_radians = np.arccos(np.clip(dot_product / norm_product, -1.0, 1.0))
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

def calculate_slope(point1, point2):
    if point2[0] == point1[0]:
        return 0.0  # or any default value you prefer
    else:
        return (point2[1] - point1[1]) / (point2[0] - point1[0])

def calculate_max_ratio(value1, value2):
    return max(value1 / value2, value2 / value1)

def calculate_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def process_landmarks(landmarks):
    # Extract the x, y coordinates of the 51 key points
    key_points = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)])

    # Feature calculations
    features = [
        calculate_angle(key_points[0], key_points[9], key_points[0]),  # f0
        calculate_angle(key_points[2], key_points[7], key_points[2]),  # f1
        calculate_angle(key_points[4], key_points[5], key_points[4]),  # f2
        max(key_points[2, 1] / key_points[7, 1], key_points[7, 1] / key_points[2, 1],
            key_points[4, 1] / key_points[5, 1], key_points[5, 1] / key_points[4, 1]),  # f3
        calculate_slope(key_points[0], key_points[9]),  # f4
        calculate_slope(key_points[2], key_points[7]),  # f5
        calculate_slope(key_points[4], key_points[5]),  # f6
        calculate_angle(key_points[10], key_points[19], key_points[10]),  # f7
        calculate_max_ratio(calculate_distance(key_points[11], key_points[13]),
                            calculate_distance(key_points[12], key_points[14])),  # f8
        calculate_max_ratio(calculate_distance(key_points[15], key_points[17]),
                            calculate_distance(key_points[16], key_points[18])),  # f9
        calculate_max_ratio(calculate_distance(key_points[19], key_points[21]),
                            calculate_distance(key_points[20], key_points[22])),  # f10
        calculate_max_ratio(calculate_distance(key_points[23], key_points[25]),
                            calculate_distance(key_points[24], key_points[26])),  # f11
        calculate_max_ratio(calculate_distance(key_points[23], key_points[37]),
                            calculate_distance(key_points[27], key_points[22])),  # f12
        calculate_max_ratio(calculate_distance(key_points[27], key_points[28]),
                            calculate_distance(key_points[29], key_points[30])),  # f13
        calculate_angle(key_points[28], key_points[34], key_points[28]),  # f14
        calculate_max_ratio(calculate_distance(key_points[31], key_points[32]),
                            calculate_distance(key_points[33], key_points[34])),  # f15
        calculate_max_ratio(calculate_distance(key_points[35], key_points[36]),
                            calculate_distance(key_points[37], key_points[38])),  # f16
        calculate_max_ratio(calculate_distance(key_points[39], key_points[40]),
                            calculate_distance(key_points[41], key_points[42])),  # f17
        calculate_max_ratio(calculate_distance(key_points[43], key_points[44]),
                            calculate_distance(key_points[45], key_points[46])),  # f18
        calculate_max_ratio(calculate_distance(key_points[48], key_points[51]),
                            calculate_distance(key_points[54], key_points[57])),  # f19
        calculate_max_ratio(calculate_distance(key_points[49], key_points[50]),
                            calculate_distance(key_points[55], key_points[56])),  # f20
        calculate_max_ratio(calculate_distance(key_points[52], key_points[53]),
                            calculate_distance(key_points[58], key_points[59])),  # f21
        calculate_angle(key_points[23], key_points[27], key_points[23]),  # f22
        calculate_angle(key_points[22], key_points[37], key_points[22]),  # f23
        calculate_max_ratio(calculate_distance(key_points[36], key_points[38]),
                            calculate_distance(key_points[37], key_points[38])),  # f24
        calculate_max_ratio(calculate_distance(key_points[52], key_points[60]),
                            calculate_distance(key_points[53], key_points[61])),  # f25
        calculate_max_ratio(calculate_distance(key_points[50], key_points[51]),
                            calculate_distance(key_points[58], key_points[59])),  # f26
        calculate_distance(key_points[46], key_points[23]) / calculate_distance(key_points[43], key_points[23]),  # f27
        calculate_distance(key_points[51], key_points[23]) / calculate_distance(key_points[48], key_points[23]),  # f28
    ]
    return features[:28]  # Keep only the first 28 elements

def resize_image(img, width=500, height=None):
    if height is None:
        # Maintain aspect ratio
        r = width / img.shape[1]
        dim = (width, int(img.shape[0] * r))
    else:
        dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

def extract_features(img, output):

    # img = resize_image(img)  # Resize the image to speed up processing

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    features = np.zeros(28)  # Initialize features with zeros

    if faces:  # Check if faces are detected
        landmarks = predictor(gray, faces[0])  # Process only the first detected face
        marked_img = mark_landmarks(img, landmarks)
        features = process_landmarks(landmarks)
        # cv2.imshow("marked",marked_img)
        output.append(marked_img)                       #storing the marked image

    return features

def mark_landmarks(img, landmarks):
    marked_img = img.copy()

    # Loop through each landmark and mark it on the image
    for point in landmarks.parts():
        x, y = point.x, point.y
        cv2.circle(marked_img, (x, y), 3, (0, 255, 0), -1)  # Mark the landmark with a green circle

    return marked_img

def load_and_predict(img, output):
    # Load the trained model
    log_model = joblib.load('voting_classifier.joblib')
#     log_model = joblib.load('backend/voting_classifier.joblib')

    # Extract features from the image
    features = extract_features(img, output)

    # Make a prediction using the trained model
    prediction = log_model.predict([features])
    output.append(prediction[0])                                #storing the prediction

    return output

# for i in range(769,790):
# img_path = f"images2/{i}.jpg"
# img_path = "845.jpg"
# img = cv2.imread(img_path)

def process_image(img): 
        
        output = []
        output = load_and_predict(img, output)          #output is an array that stores the marked img as the first element and the prediction as the second element
        print(f"Prediction: {output[1]}")
        return output
