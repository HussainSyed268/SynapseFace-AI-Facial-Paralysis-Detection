# SynapseFace

SynapseFace is an AI-driven facial paralysis detection project that employs advanced facial landmark extraction techniques and machine learning models to differentiate between faces with and without facial paralysis.

## Overview

The project utilizes the following technologies:
- **Backend**: Built on Flask, handling server-side functionalities.
- **Frontend**: Developed using React JS, Tailwind CSS, and Daisy UI for an interactive user interface.

## Facial Paralysis Detection Process

1. **Facial Landmark Extraction**: Utilizes dlib and cv2 libraries in Python to extract 68 facial landmarks.
2. **Feature Extraction**: Derives 28 facial features (e.g., eyebrow distance, nose distances, lips slope, facial angles) from these landmarks.
3. **Machine Learning Models**: An ensemble of SVM, Random Forest, and Gradient Boosting models is trained on the extracted facial features.
   
## Data and Model Performance

- **Dataset**: Included 2524 images; 208 were used for testing due to privacy concerns.
- **Model Performance**:
  - Accuracy: 88%
  - F1 Score: 81%
  - Precision: 85%
  - Recall: 76%
 
## User Interface

![image](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/ef28fb10-9ba1-4f99-acba-7afe792d8035)

![Screenshot from 2023-12-30 00-47-25](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/91bcc43d-ff28-454d-9075-e8d71d94f7bb)

![Screenshot from 2023-12-30 00-48-00](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/7f4fabd7-876a-474b-a126-90773be2e10e)

![image](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/f21f1c41-8607-48b7-956c-f09798517632)

![image](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/295f5ef1-afc7-4066-961f-02fc94a1ec38)

![image](https://github.com/HussainSyed268/SynapseFace-AI-Facial-Paralysis-Detection/assets/100157373/e9be0d63-d702-4d4a-9f94-94b67ce7a7e6)


## Future Improvements

As the dataset was limited due to privacy concerns, expanding the dataset is crucial for enhancing accuracy in future iterations.

## Folders

- **Backend**: Contains the Flask-based server-side logic for SynapseFace.
- **Frontend**: Hosts the React-based user interface components using Tailwind CSS and Daisy UI.

## Installation

1. Navigate to the `backend` directory and develop a python virtual environment using python3 -m venv .venv.
2. Activate the virtual environment using . .venv/bin/activate
3. Install the dependencies for the backend
4. Go to the `frontend` directory and run npm i to install the dependencies.

## Getting Started

1. Run the backend server by running app.py using python3 app.py in the virtual environment.
2. Launch the frontend application using npm run start.

## Contributions

Contributions are welcomed! Please feel free to submit issues and pull requests.
