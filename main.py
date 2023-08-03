import cv2 as cv
import numpy as np

import refine

def process_image(path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, vertices = refine.detect_edges(path)

        if refined_image is not None:
            # Show the refined image
            cv.imshow('Refined', refined_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print(f"No object detected in {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

def main():
    # List of image paths to process
    image_paths = [
        'src/test/photo.jpg',
        'src/test/machamp.jpeg',
        'src/test/greve.jpeg',
        'src/test/greve3.jpeg'
    ]

    for path in image_paths:
        process_image(path)

if __name__ == "__main__":
    main()
