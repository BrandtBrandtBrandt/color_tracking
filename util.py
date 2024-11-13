import numpy as np
import cv2

def get_limits(color):
    # Convert BGR color input to a numpy array with shape (1, 1, 3) for cv2 conversion
    c = np.uint8([[color]])
    
    # Convert BGR to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper limits for hue range with fixed saturation and value ranges
    lowerLimit = hsvC[0][0][0] - 10, 150, 100  # Lower HSV boundary
    upperLimit = hsvC[0][0][0] + 10, 255, 255  # Upper HSV boundary
    
    # Convert limits to numpy arrays for OpenCV compatibility
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    return lowerLimit, upperLimit