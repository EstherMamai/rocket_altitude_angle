import math

# Calculate the angle of elevation of the rocket in degrees
def calculate_angle_of_elevation(camera_fov, frame_height, bounding_box_center_y):
    """
    Calculates the angle of elevation of the rocket based on the bounding box coordinates.
    :param camera_fov: Vertical field of view of the camera (in degrees).
    :param frame_height: Height of the video frame (in pixels).
    :param bounding_box_center_y: Y-coordinate of the center of the bounding box (in pixels).
    :return: Angle of elevation in degrees.
    """
    # Calculate the angular resolution per pixel
    angular_resolution_per_pixel = camera_fov / frame_height
    
    # Find the pixel offset from the bottom of the frame
    pixel_offset_from_bottom = frame_height - bounding_box_center_y
    
    # Calculate the angle of elevation
    angle_of_elevation = pixel_offset_from_bottom * angular_resolution_per_pixel
    return angle_of_elevation

# Calculate the altitude of the rocket based on the angle of elevation
def calculate_altitude(camera_distance, angle_of_elevation):
    """
    Calculates the altitude of the rocket using trigonometry.
    :param camera_distance: Distance from the camera to the rocket's launch site (in meters).
    :param angle_of_elevation: Angle of elevation (in degrees).
    :return: Altitude in meters.
    """
    # Convert angle from degrees to radians for trigonometric calculation
    angle_in_radians = math.radians(angle_of_elevation)
    
    # Use trigonometry (tan) to calculate the altitude
    altitude = math.tan(angle_in_radians) * camera_distance
    return altitude
