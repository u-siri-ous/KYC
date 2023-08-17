import cv2 as cv
import numpy as np

data = []
jungle = cv.imread('src/test/expansions/jungle.jpg')
fossil = cv.imread('src/test/expansions/fossil.jpg')    #this image in png is featureless
data.append(jungle)
data.append(fossil)

classes = ['jungle', 'fossil', 'base']

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
# [[-1, -1, -1],[-1, 8, -1],[-1, -1, 0]]

contrast = 2 # Contrast control ( 0 to 127)
brightness = 1 # Brightness control (0-100)

def findexp(symbol):
    descriptors = data_desc(data)
    sharpened = cv.filter2D(symbol, -1, kernel) #the image is small, we need to sharpen it
    #cv.imshow('sharpened', sharpened)
    #dark = cv.addWeighted(sharpened, contrast, sharpened, 0, brightness)
    #gray = cv.cvtColor(sharpened, cv.COLOR_BGR2GRAY)
    cv.imshow('dark/sharp', sharpened)
    classID = classify_exp(sharpened, descriptors)
    print(classes[classID])
    return classes[classID]

def data_desc(lst):
    data_lst = []
    sift = cv.SIFT_create(nfeatures=2000)

    for exp in lst:
        _, des = sift.detectAndCompute(exp, None)
        
        data_lst.append(des)

    return data_lst

def classify_exp(image, desc_list):
    sift = cv.SIFT_create(nfeatures=2000)
    _, des_image = sift.detectAndCompute(image, None)

    matcher = cv.BFMatcher(cv.NORM_L2)
    best_matches = []

    for desc in desc_list:
        matches = matcher.knnMatch(des_image, desc, k=2)
        good_match = []

        for m, n in matches:
            #print(m.distance, n.distance)
            if m.distance < n.distance * 0.95:
                good_match.append([m])

        best_matches.append(len(good_match))
    
    classID = -1

    print(best_matches)

    if len(best_matches):
        if max(best_matches) > 6:
            classID = best_matches.index(max(best_matches))

    return classID