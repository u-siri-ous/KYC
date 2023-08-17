import cv2 as cv
import refine
from expansion import findexp
import grader

def process_single_image(image_path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, vertices, network_input, symbol = refine.detect_edges(image_path)
        # detected_symbol = findexp(symbol)

        if refined_image is not None:
            # Show the refined image
            cv.imshow('Refined', refined_image)
            cv.imshow('Neural network', network_input)
            cv.imshow('Symbol', symbol)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print(f"No object detected in '{image_path.split('/')[-1].split('.')[0]}'")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_image_paths(image_paths):
    for path in image_paths:
        grader.centering(path)
        process_single_image(path)
        pass

def main():
    # List of image paths to process
    image_paths = [
        'images/test/electrode.jpeg',  #-----JUNGLE-----  foderina
        'images/test/geodude.jpeg',    #-----FOSSIL-----  foderina
        'images/test/grimer.jpeg',     #-----FOSSIL-----, problematico con le coordinate, foderina
        'images/test/kangaskhan.jpeg', #-----JUNGLE-----, foderina
        'images/test/krabby.jpeg',     #-----FOSSIL-----, si incasina con lo sharpen
        'images/test/machamp.jpg',     #------BASE------
        'images/test/machoke.jpg',     #------BASE------
        'images/test/mankey.jpeg',     #-----JUNGLE-----, foderina
        'images/test/pikachu.jpg',     #-----JUNGLE-----
        'images/test/ponyta.jpg',      #------BASE------, problematico con le coordinate
        'images/test/psyduck.jpg',     #-----FOSSIL-----
        'images/test/staryu.jpg',      #------BASE------
        'images/test/vulpix.jpg',      #------BASE------
        'images/test/weedle.jpg',      #------BASE------
    ]

    process_image_paths(image_paths)

if __name__ == "__main__":
    main()
