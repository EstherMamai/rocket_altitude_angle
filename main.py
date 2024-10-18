import cv2
from roboflow import Roboflow
import csv
from calculate import calculate_angle_of_elevation, calculate_altitude

# Initialize Roboflow with your API key
rf = Roboflow(api_key="amLDwnyGfdSsvyilDr0g")
project = rf.workspace("nasaspaceflight").project("rocket-detect")
model = project.version("2").model

# Open the video file
video_path = "rocket_launch.mp4"  # Replace with your video path
cap = cv2.VideoCapture(video_path)


# Camera and rocket parameters
camera_fov_vertical = 60  # Vertical field of view of the camera in degrees
frame_height = 1080  # Height of the video frame in pixels
camera_distance_to_rocket = 100  # Distance from the camera to the rocket's launch point in meters

# Placeholder for bounding box coordinates (you'll replace this with your YOLO model output)
bounding_boxes = [
    {"frame": 1, "center_x": 500, "center_y": 600, "width": 50, "height": 120},
    {"frame": 2, "center_x": 510, "center_y": 580, "width": 50, "height": 120},
    {"frame": 3, "center_x": 520, "center_y": 560, "width": 50, "height": 120},
    # Add more bounding box entries here as needed...
]

# Open CSV file for writing predictions
with open('rocket_tracking_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['frame_number', 'center_x', 'center_y', 'width', 'height', 'angle_of_elevation', 'altitude'])

    # Process each bounding box entry
    for bbox in bounding_boxes:
        frame = bbox['frame']
        center_x = bbox['center_x']
        center_y = bbox['center_y']
        width = bbox['width']
        height = bbox['height']

        # Calculate angle of elevation and altitude
        angle_of_elevation = calculate_angle_of_elevation(camera_fov_vertical, frame_height, center_y)
        altitude = calculate_altitude(camera_distance_to_rocket, angle_of_elevation)

        # Write frame, bounding box, angle, and altitude to CSV
        writer.writerow([frame, center_x, center_y, width, height, angle_of_elevation, altitude])

print("Tracking data saved to 'rocket_tracking_data.csv'.")
