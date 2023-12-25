import dlib
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, recall_score
import joblib

detector = dlib.get_frontal_face_detector()
predictor_path = 'shape_predictor_68_face_landmarks.dat'  # Replace with the actual path
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


def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE to the L-channel
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    l_clahe = clahe.apply(l)

    # Merge the CLAHE-enhanced L-channel with the original A and B channels
    lab_clahe = cv2.merge((l_clahe, a, b))

    # Convert LAB back to BGR
    result = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

    return result


def extract_features(img):
    # gray = apply_clahe(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    features = np.zeros(28)  # Initialize features with zeros

    if faces:  # Check if faces are detected
        landmarks = predictor(gray, faces[0])  # Process only the first detected face
        features = process_landmarks(landmarks)

    return features

def train_and_save_models(data_paths, labels):
    X_train = []
    X_train_models = []
    models = []

    for image_path in data_paths:
        img = cv2.imread(image_path)
        print(image_path)

        features = extract_features(img)
        X_train.append(features)

    X_train = np.vstack(X_train)
    X_train_models.append(X_train)
    y_train = labels

    # Train the SVM model
    svm_model = SVC(kernel='rbf', C=10000, gamma=0.001 , probability=True )
    svm_model.fit(X_train, y_train)
    models.append(('svm', svm_model))

    # Train a Random Forest model
    random_forest = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    random_forest.fit(X_train, y_train)
    models.append(('random_forest', random_forest))

    # Train a Gradient Boosting model
    gradient_boosting = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    gradient_boosting.fit(X_train, y_train)
    models.append(('gradient_boosting', gradient_boosting))

    return models, X_train_models

# Load your dataset, where '1' represents paralyzed and '0' represents not paralyzed
# Replace with the actual paths and labels of your dataset
data_paths = []

for i in range(1, 2308):
    if (((i >= 693) and (i <= 792)) or (i>=1629) and (i<=1728)):
        continue
    else:
        data_paths.append(f"safviDS/{i}.jpg")

d1 = np.zeros(692)
d2 = np.ones(836)
d3 = np.zeros(579)
labels = np.concatenate((d1, d2, d3))

# Split the dataset into training and testing sets
X_train_paths, X_test_paths, y_train, y_test = train_test_split(
    data_paths, labels, test_size=0.2, random_state=42
)

# Train the models and save them to files
models, X_train_models = train_and_save_models(X_train_paths, y_train)

# Create a Voting Classifier
voting_classifier = VotingClassifier(estimators=models, voting='soft')

# Train the Voting Classifier
voting_classifier.fit(X_train_models[0], y_train)

# Save the trained Voting Classifier to a file
joblib.dump(voting_classifier, 'voting_classifier.joblib')

# Load the trained Voting Classifier
ensemble_model = joblib.load('voting_classifier.joblib')

# Iterate through the test images and make predictions using the ensemble model
ensemble_predictions = []

for test_path in X_test_paths:
    test_img = cv2.imread(test_path)
    ensemble_prediction = ensemble_model.predict([extract_features(test_img)])
    ensemble_predictions.append(ensemble_prediction[0])

# Convert ensemble predictions to a numpy array for consistency
ensemble_predictions = np.array(ensemble_predictions)

# Calculate accuracy, F1 score, confusion matrix, and recall for the ensemble model
ensemble_accuracy = accuracy_score(y_test, ensemble_predictions)
ensemble_f1 = f1_score(y_test, ensemble_predictions)
ensemble_conf_matrix = confusion_matrix(y_test, ensemble_predictions)
ensemble_recall = recall_score(y_test, ensemble_predictions)

print(f"Ensemble Accuracy: {ensemble_accuracy * 100:.2f}%")
print(f"Ensemble F1 Score: {ensemble_f1:.2f}")
print(f"Ensemble Confusion Matrix:\n{ensemble_conf_matrix}")
print(f"Ensemble Recall: {ensemble_recall:.2f}")