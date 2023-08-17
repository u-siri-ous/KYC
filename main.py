import cv2 as cv
import numpy as np

import refine
from expansion import findexp

def process_image(path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, vertices, network_input, symbol = refine.detect_edges(path)
        detected_symbol = findexp(symbol)

        if refined_image is not None:
            # Show the refined image
            #cv.imshow('Refined', refined_image)
            #cv.imshow('Neural network', network_input)
            cv.imshow('Symbol', symbol)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print(f"No object detected in '{path.split('/')[-1].split('.')[0]}'")
    except Exception as e:
        print(f"Error processing {path}: {e}")

def main():
    # List of image paths to process
    image_paths = [
        #-----BASE-----
        'src/test/weedle.jpg',
        'src/test/machamp.jpg',
        'src/test/machoke.jpg',
        #'src/test/ponyta.jpg', #problematico con le coordinate
        'src/test/vulpix.jpg',
        'src/test/staryu.jpg',
        #-----FOSSIL-----
        'src/test/psyduck.jpg',
        'src/test/krabby.jpeg', # si incasina con lo sharpen
        'src/test/geodude.jpeg', #foderina
        #'src/test/grimer.jpeg', #problematico con le coordinate, foderina
        #-----JUNGLE-----
        'src/test/pikachu.jpg',
        'src/test/electrode.jpeg', #foderina
        'src/test/kangaskhan.jpeg', #foderina
        'src/test/mankey.jpeg' #foderina
    ]

    for path in image_paths:
        process_image(path)

if __name__ == "__main__":
    main()
