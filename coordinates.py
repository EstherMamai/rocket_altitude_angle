import cv2
from roboflow import Roboflow
import csv

# Initialize Roboflow with your API key
rf = Roboflow(api_key="amLDwnyGfdSsvyilDr0g")
project = rf.workspace("nasaspaceflight").project("rocket-detect")
model = project.version("2").model

# Open the video file
video_path = "rocket_launch.mp4"  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Open CSV file for writing predictions
with open('predictions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['frame_number', 'class', 'x', 'y', 'width', 'height', 'confidence'])

    # Process video frame by frame
    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame to a temporary image file
        frame_path = "temp_frame.jpg"
        cv2.imwrite(frame_path, frame)

        # Run prediction on the saved frame
        predictions = model.predict(frame_path, confidence=40, overlap=30).json()

        # Write predictions to the CSV file
        for prediction in predictions['predictions']:
            writer.writerow([
                frame_number,
                prediction['class'],
                prediction['x'],
                prediction['y'],
                prediction['width'],
                prediction['height'],
                prediction['confidence']
            ])

        frame_number += 1

# Release everything
cap.release()
cv2.destroyAllWindows()
