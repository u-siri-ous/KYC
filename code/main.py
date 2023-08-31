import cv2 as cv
from grader.valutator import grading
from grader.refine import detect_edges
from GUI.GUI import GUI

def process_single_image(image_path):
    try:
        # Get the refined image and vertices from the 'refine' module
        refined_image, card, network_input, symbol = detect_edges(image_path)
        # detected_symbol = findexp(symbol)

        if card is not None:
            # Show the refined image
            # cv.imshow('Refined', card)
            # cv.imshow('Neural input', network_input)
            cv.imwrite('code/card.jpg', card)
            # cv.imshow('Symbol', symbol)
            cv.waitKey(0)
            cv.destroyAllWindows()
            return card, network_input
        else:
            print(f"No object detected in '{image_path.split('/')[-1].split('.')[0]}'")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_image_paths(image_paths):
    for path in image_paths:
        cen, cor, edg, sur = grading(path)
        process_single_image(path)
        # nnFunction(network_input)
        GUI(cen, cor, edg, sur)

def main():
    # List of image paths to process
    image_paths = [
        #'images/grader_test/electrode.jpeg',
        #'images/grader_test/geodude.jpeg'
        # 'images/grader_test/pikachu.jpg'
        #'images/grader_test/kangaskhan.jpeg'
        # 'images/grader_test/machamp.jpg'
        #'images/grader_test/grimer.jpeg'
        #'images/grader_test/machoke.jpg'
        #'images/grader_test/ponyta.jpg'
        'images/grader_test/psyduck.jpg'
        #'images/grader_test/staryu.jpg'
        #'images/grader_test/vulpix.jpg'
        #'images/grader_test/weedle.jpg'
        #'images/grader_test/mankey.jpeg'
        #'images/grader_test/krabby.jpeg'
        #'cards/jungle_test/vaporeon_test.png'
        #'cards/Fossil/grimer.png' #worst case non funziona un c
        #'/Users/leonardvincentramil/Desktop/BaseCards/Blastoice_card.png'
        #'/Users/leonardvincentramil/Documents/GitHub/KYC/cards/jungle_test/nidoran_f_test.png'
    ]

    process_image_paths(image_paths)

if __name__ == "__main__":
    main()

'''
        'images/test/electrode.jpeg',  #-----JUNGLE-----  foderina
        'images/test/geodude.jpeg',    #-----FOSSIL-----  foderina
        'images/test/grimer.jpeg',     #-----FOSSIL-----, problematico con le coordinate, foderina
        'images/test/kangaskhan.jpeg', #-----JUNGLE-----, foderina
        'images/test/krabby.jpeg',     #-----FOSSIL-----, si incasina con lo sharpen
        'images/test/machamp.jpg',     #------BASE------
        'images/test/machoke.jpg',     #------BASE------
        'images/test/mankey.jpeg',     #-----JUNGLE-----, foderina
        'images/test/ponyta.jpg',      #------BASE------, problematico con le coordinate
        'images/test/psyduck.jpg',     #-----FOSSIL-----
        'images/test/staryu.jpg',      #------BASE------
        'images/test/vulpix.jpg',      #------BASE------
        'images/test/weedle.jpg',      #------BASE------
        'images/test/pikachu.jpg',     #-----JUNGLE-----
'''