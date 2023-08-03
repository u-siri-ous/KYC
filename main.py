import cv2 as cv
import numpy as np

import refine

def main(path):
    card = refine.cropped(path)
    cv.imshow('refined', card)
    cv.waitKey(0)
    cv.destroyAllWindows()


main('src/test/photo.jpg')
main('src/test/machamp.jpeg')