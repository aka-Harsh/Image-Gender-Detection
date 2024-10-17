import cv2
import numpy as np
import csv
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

def load_models():
    # Load face detection model 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load our custom gender classification model
    gender_model = load_model('models/gender_classification_model.h5')
    
    return face_cascade, gender_model

def detect_and_classify_gender(frame, face_cascade, gender_model):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    results = []
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = cv2.resize(face, (150, 150))
        face = img_to_array(face)
        face = np.expand_dims(face, axis=0)
        face = face / 255.0
        
        gender_pred = gender_model.predict(face)[0][0]
        gender = "Female" if gender_pred < 0.5 else "Male"
        
        results.append((x, y, x+w, y+h, gender))
    
    return results

def draw_results(frame, results):
    for (x1, y1, x2, y2, gender) in results:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, gender, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return frame

def save_image(frame, gender):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"captured_images/{gender}_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    return filename

def update_csv(filename, gender):
    with open('captured_images/log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([filename, gender])
