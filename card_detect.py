import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    # Blur the image 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
    
    # Detect edges 
    edges = cv2.Canny(blurred, 50, 150) 
    
    # Find contours 
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    # Filter contours 
    rects = [] 
    for contour in contours: 
        # Approximate the contour to a polygon 
        polygon = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True) 
        
        # Check if the polygon has 4 sides and the aspect ratio is close to 1 
        if len(polygon) == 4 and abs(1 - cv2.contourArea(polygon) / (cv2.boundingRect(polygon)[2] * cv2.boundingRect(polygon)[3])) < 0.1: 
            rects.append(polygon) 
    
    # Draw rectangles 
    for rect in rects: 
        cv2.drawContours(frame, [rect], 0, (0, 255, 0), 3) 
        draw_rect = cv2.boundingRect(rect)
        cv2.rectangle(frame, draw_rect, (0,0,255), 3)

    #LA VITA
    #r = cv2.selectROI(frame, showCrosshair=False)
    #card = frame[int(r[1]):int(r[1]+r[3]), 
    #             int(r[0]):int(r[0]+r[2])]

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    k = cv2.waitKey(30)
    if k == ord("q"):  
        break