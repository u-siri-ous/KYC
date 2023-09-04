import cv2 as cv
from grader.valutator import grading
from grader.refine import detect_edges
from GUI.GUI import GUI
from NN.mainNN import classify_pokemon

def process_single_image(image_path):
    try:
        _, card, network_input = detect_edges(image_path)
        if card is not None:
            cv.imwrite('code/card.jpg', card)
            return card, network_input
        else:
            print(f"No object detected in the photo!")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_and_display_images(image_paths):
    for path in image_paths:
        try:
            cen, cor, edg, sur = grading(path)
            card, network_input = process_single_image(path)
            if card is not None:
                p_name = classify_pokemon(network_input, 'data/models/model3.h5', (64, 64))
                GUI(p_name, cen, cor, edg, sur)
        except Exception as e:
            print(f"Error processing {path}: {e}")

def main():
    image_paths = [
        'images/grader_test/weedle.jpg',
        # Add more image paths here
    ]

    process_and_display_images(image_paths)

if __name__ == "__main__":
    main()