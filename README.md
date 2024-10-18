# Rocket Tracking and Altitude Calculation Project

This project aims to track a rocket's trajectory using a pretrained YOLOv5 object detection model from Roboflow. The bounding box coordinates of the rocket are used to calculate the rocket's altitude and angle of elevation in real-time as it ascends. These values are saved to a CSV file for further analysis.

## Features
- **Real-time Rocket Tracking**: The YOLOv5 model detects the rocket in each frame of a video and outputs its bounding box coordinates.
- **Angle of Elevation Calculation**: Based on the bounding box location in the frame, the project calculates the rocket's angle of elevation using the camera's field of view.
- **Altitude Calculation**: The altitude of the rocket is determined using the angle of elevation and the known distance from the camera to the launch site.
- **CSV Logging**: The bounding box coordinates, angle of elevation, and altitude are saved to a CSV file for easy analysis.

## Project Structure
```
.
├── calculate.py           # Contains functions to calculate angle of elevation and altitude
├── main.py                # Main script to process video, calculate data, and save results
├── rocket_tracking_data.csv # Sample output CSV file (generated after running the main.py)
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```

## Setup Instructions

### Prerequisites
1. **Python 3.10 or above**.
2. You will need the following Python libraries:
   - `roboflow`
   - `opencv-python`
   - `numpy`
   - `Pillow`
   - `math`
   - `csv`

   You can install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

### Step-by-Step Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/EstherMamai/rocket-tracking.git
   cd rocket-tracking
   ```

2. **Install dependencies**:
   Ensure that you have all the required libraries installed by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Script**:
   Once everything is set up, you can run the main script (`main.py`) which will:
   - Read bounding box coordinates from the YOLOv5 model output.
   - Calculate the angle of elevation and altitude for each frame.
   - Write the results to a CSV file (`rocket_tracking_data.csv`).

   Use the following command to run the main script:
   ```bash
   python main.py
   ```

### Configuration

- **Camera Parameters**: 
   Adjust the following parameters in `main.py` to match your camera setup:
   - `camera_fov_vertical`: The vertical field of view (FOV) of your camera (in degrees).
   - `frame_height`: The height of the video frame (in pixels).
   - `camera_distance_to_rocket`: The distance from the camera to the rocket launch site (in meters).

- **Bounding Box Data**:
   Replace the sample bounding box data in `main.py` with your YOLOv5 model’s output.

## Example Output

The CSV output will look like this:

```
frame_number,center_x,center_y,width,height,angle_of_elevation,altitude
1,500,600,50,120,26.67,50.52
2,510,580,50,120,30.00,57.74
3,520,560,50,120,33.33,66.67
```

This data contains:
- **frame_number**: The frame number from the video.
- **center_x** and **center_y**: The center of the bounding box representing the rocket's location in the frame.
- **width** and **height**: The dimensions of the bounding box.
- **angle_of_elevation**: The angle of elevation of the rocket based on the bounding box position.
- **altitude**: The calculated altitude of the rocket.

## How it Works

### 1. **Rocket Detection Using YOLOv5**:
   The pretrained YOLOv5 model detects the rocket in each video frame and provides the bounding box coordinates of the rocket. These bounding boxes specify where the rocket is located within the frame.

### 2. **Angle of Elevation Calculation**:
   Using the vertical field of view (FOV) of the camera and the bounding box's center Y-coordinate, the system calculates the angle of elevation of the rocket.

### 3. **Altitude Calculation**:
   Using trigonometry, the system calculates the rocket's altitude from the camera's distance to the launch site and the calculated angle of elevation.

### 4. **Logging Results to CSV**:
   The bounding box coordinates, angle of elevation, and calculated altitude for each frame are saved to a CSV file for easy analysis.

## Future Work
- Integrating real-time video processing for live rocket tracking.
- Implementing 3D trajectory reconstruction from multiple camera angles.
- Visualizing the rocket's flight path using graphing libraries.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

### Contributions

Feel free to contribute by submitting pull requests, reporting issues, or suggesting improvements.

## Contact
For any questions, reach out via [LinkedIn](https://www.linkedin.com/in/esther-mamai/) or check out more projects on [GitHub](https://github.com/EstherMamai)
