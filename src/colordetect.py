import cv2
import numpy as np

def detect_color_edge(image):
    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Split HSV channels
    hue, saturation, value = cv2.split(hsv_image)
    
    # Example: detect edges based on the hue channel
    edges = cv2.Canny(hue, 50, 150)
    
    return edges

# Example usage:
image = cv2.imread('Screenshot13.png')
edges = detect_color_edge(image)
screen_w, screen_h = edges.shape[::-1]
cropped_edges = edges[round(screen_h*0.48):round(screen_h*0.53), round(screen_w*0.4):round(screen_w*0.605)]
cv2.imshow('Color Edges', cropped_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()