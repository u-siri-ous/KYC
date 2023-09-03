import cv2 as cv
from grader.valutator import grading
from grader.refine import detect_edges
from GUI.GUI import GUI
from NN.mainNN import classify_pokemon


def process_single_image(image_path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, card, network_input= detect_edges(image_path)
        # detected_symbol = findexp(symbol)

        if card is not None:
            cv.imwrite('code/card.jpg', card)
            return card, network_input
        else:
            print(f"No object detected in '{image_path.split('/')[-1].split('.')[0]}'")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_image_paths(image_paths):
    for path in image_paths:
        cen, cor, edg, sur = grading(path)
        card, network_input = process_single_image(path)
        p_name  = classify_pokemon(network_input, 'data/models/model3.h5', (64,64))
        GUI(p_name, cen, cor, edg, sur)
        

def main():
    # List of image paths to process
    image_paths = [
        'images/grader_test/electrode.jpeg'
        # 'images/grader_test/geodude.jpeg',
        # 'images/grader_test/pikachu.jpg',
        # 'images/grader_test/kangaskhan.jpeg', 0 danno
        # 'images/grader_test/machamp.jpg' # da rirunnare
        # 'images/grader_test/grimer.jpeg', foto non valida
        # 'images/grader_test/machoke.jpg',
        # 'images/grader_test/ponyta.jpg',
        # 'images/grader_test/psyduck.jpg',
        # 'images/grader_test/staryu.jpg',
        # 'images/grader_test/vulpix.jpg',
        # 'images/grader_test/anonymous_vulpix.jpg'
        # 'images/grader_test/weedle.jpg',
        # 'images/grader_test/mankey.jpeg',
        # 'images/grader_test/krabby.jpeg'
    ]

    process_image_paths(image_paths)

if __name__ == "__main__":
    main()