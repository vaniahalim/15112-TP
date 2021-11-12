from handTrackingMod import *
import cv2
import numpy as np
import time
import os

# header image (color picker, countertop design)
# choose colour to draw
drawColor = ()

# painter config
brushThickness = 15

# open camera
cap = cv2.VideoCapture(0) 
# change size of camera screen
cap.set(3, 500) # =width
cap.set(4, 720)  #height

# initialize detector class
detector = handDetector(detectionCon = 0.8)
# initialize starting location
x_prev, y_prev = 0, 0
# draw on canvas instead of camera screen
imgCanvas = np.zeros((720,1280,3), np.uint8)

while True:
    # import image
    success, img = cap.read() # get video
    img = cv2.flip(img, 1) # mirror image

    # find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,0) # get landmark positions

    if len(lmList) != 0: # if landmark on screen
        # print(lmList[4]) # int based on which landmark you want -> prints pos of that landmark

        x_index, y_index = lmList[8][1:]
        x_mid, y_mid = lmList[12][1:]

        # check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers) # list of which fingers are up

        # selection mode: 2 fingers are up
        if fingers[1] == 1 and fingers[2] == 1:
            x_prev, yprev = 0, 0 # reset position of finger everytime you select
        
            print("select a color!")
            # select colour

        # drawing mode: index finger is up
        if fingers[1]==1 and fingers[2] == 0:
            print("draw!")
            drawColor = (255,255,255) # choose color (white currently)
            cv2.circle(img, (x_index, y_index), 15, drawColor, cv2.FILLED)
            
            # update previous point 
            if x_prev == 0 and y_prev == 0:
                x_prev, y_prev = x_index, y_index

            cv2.line(img, (x_prev, y_prev), (x_index, y_index), drawColor, brushThickness)
            cv2.line(imgCanvas, (x_prev, y_prev), (x_index, y_index), drawColor, brushThickness)
     
        x_prev, y_prev = x_index, y_index # keep updating position of fingers

    cv2.putText(img, "Draw here!", (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Latte art!", img)
    cv2.imshow("Canvas", imgCanvas) # show canvas of drawing
    cv2.waitKey(1) # 0 gives still images

