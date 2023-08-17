import cv2 as cv
import numpy as np

def detect_edges(image_path):
    try:
        # Load the image
        image = cv.imread(image_path)

        # Resize the image to half of its original size
        card = cv.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

        # Convert the resized image from BGR to HSV color space
        hsv_image = cv.cvtColor(card, cv.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the yellow color in HSV
        lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
        upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

        # Create a binary mask where pixels falling within the yellow color range become white (255) and others black (0)
        mask = cv.inRange(hsv_image, lower_yellow, upper_yellow)

        # Find contours in the binary mask
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            # Get the bounding rectangle of the largest contour
            x, y, w, h = cv.boundingRect(max(contours, key=cv.contourArea))

            # Saving image to perform calculations
            # cv.imwrite("cropped_card.jpg", card[y:y+h, x:x+w])

            # Return the cropped region of the cropped mask and the bounding rectangle coordinates
            return mask[y:y+h, x:x+w], (x, y, w, h), card[y:y+h, x:x+w][h//6 : h//2, w//8 : (8*w)//10], card[y:y+h, x:x+w][h//2 : (h*3)//5 , (w*5)//6 : (w*19)//20]
        else:
            # Return None if no yellow object is detected
            return None, None, None, None

    except Exception as e:
        # Handle any errors that may occur during the processing
        print("Error:", e)
        return None, None, None, None