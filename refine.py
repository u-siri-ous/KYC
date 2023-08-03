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
        upper_yellow = np.array([25, 255, 255], dtype=np.uint8)

        # Create a binary mask where pixels falling within the yellow color range become white (255) and others black (0)
        mask = cv.inRange(hsv_image, lower_yellow, upper_yellow)

        # Find contours in the binary mask
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            # Get the bounding rectangle of the first contour (assuming only one contour is found)
            x, y, w, h = cv.boundingRect(contours[0])

            # Draw a blue rectangle around the detected region on the mask
            cv.rectangle(mask, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Return the cropped region of the original image and the bounding rectangle coordinates
            return mask[y:y+h, x:x+w], (x, y, w, h)
        else:
            # Return None if no yellow object is detected
            return None, None

    except Exception as e:
        # Handle any errors that may occur during the processing
        print("Error:", e)
        return None, None

# Usage example:
# cropped_image, bounding_rect = detect_and_crop_yellow_object("path_to_image.jpg")
# if cropped_image is not None:
#     cv.imshow('Cropped Image', cropped_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     print("Bounding Rectangle Coordinates:", bounding_rect)
# else:
#     print("No yellow object detected in the image.")
