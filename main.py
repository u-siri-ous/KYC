import cv2 as cv
import numpy as np

import refine

def process_image(path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, vertices, network_input = refine.detect_edges(path)

        if refined_image is not None:
            # Show the refined image
            cv.imshow('Refined', refined_image)
            cv.imshow('Neural network', network_input)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print(f"No object detected in '{path.split('/')[-1].split('.')[0]}'")
    except Exception as e:
        print(f"Error processing {path}: {e}")

def main():
    # List of image paths to process
    image_paths = [
        'src/test/weedle.jpg',
        'src/test/machamp.jpg',
        # 'src/test/greve.jpg',
        # 'src/test/greve3.jpg',
        'src/test/psyduck.jpg',
        'src/test/pikachu.jpg',
    ]

    for path in image_paths:
        process_image(path)

if __name__ == "__main__":
    main()
