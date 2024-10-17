import streamlit as st
import cv2
import numpy as np
from main import load_models, detect_and_classify_gender, draw_results, save_image, update_csv

def main():
    st.title("Real-Time Gender Detection")

    face_cascade, gender_model = load_models()

    capture_button = st.button("Capture and Save")
    capture_placeholder = st.empty()

    # OpenCV video capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame from camera")
            break

        results = detect_and_classify_gender(frame, face_cascade, gender_model)
        frame_with_results = draw_results(frame, results)

        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame_with_results, cv2.COLOR_BGR2RGB)

        # Display the frame
        capture_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        if capture_button:
            if results:
                for (x1, y1, x2, y2, gender) in results:
                    face = frame[y1:y2, x1:x2]
                    filename = save_image(face, gender)
                    update_csv(filename, gender)
                st.success(f"Captured and saved {len(results)} face(s)!")
            else:
                st.warning("No faces detected. Please try again.")
            capture_button = False

        cv2.waitKey(1)

    cap.release()

if __name__ == "__main__":
    main()
