import cv2 as cv
import numpy as np

def cropped(image_path):
    # Load the image
    image = cv.imread(image_path)
    card = cv.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
    hsv_image = cv.cvtColor(card, cv.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([25, 255, 255], dtype=np.uint8)
    mask = cv.inRange(hsv_image, lower_yellow, upper_yellow)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    x,y,w,h = cv.boundingRect(contours[0]) # maybe we should add an if len(contours) == 1
    cv.rectangle(mask,(x,y),(x+w,y+h),(255,0,0),2)
    return mask[y:y+h, x:x+w]

# hsv_image[mask == 0] = (0, 0, 0)  # Set non-black pixels in the mask to black in the original image
# restored_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
# cv.imshow('Processed Image', hsv_image)