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
            largest_contour = max(contours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(largest_contour)

            # Calculate the regions of interest
            cropped_mask = mask[y:y+h, x:x+w]
            cropped_card = card[y:y+h, x:x+w]
            cropped_details = cropped_card[h//6 : h//2, w//8 : (8*w)//10]

            # Return the cropped mask, cropped card, and cropped details along with bounding rectangle coordinates
            return cropped_mask, cropped_card, cropped_details
        else:
            # Return None if no yellow object is detected
            return None, None, None, None

    except Exception as e:
        # Handle any errors that may occur during the processing
        print("Error:", e)
        return None, None, None, None