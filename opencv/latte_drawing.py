import handTrackingMod as htm
import cv2
import numpy as np
import time
import os

# open camera
cap = cv2.VideoCapture(0) # can change to 1
# change size of camera screen
cap.set(3, 500) #width
cap.set(4, 720)  #height

while True:
    # get image
    success, img = cap.read()
    # img = detector.findHands(img)
    # lmList = detector.findPosition(img,0)

    # if len(lmList) != 0: # if landmark on screen
    #     print(lmList[4]) # int based on which landmark you want -> prints pos of that landmark

    cv2.putText(img, "Draw here!", (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Latte art!", img)
    cv2.waitKey(1) # 0 gives still images

# initialize detector class
detector = handDetector()
