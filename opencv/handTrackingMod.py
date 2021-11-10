# latte art with OpenCV

# hand-tracking module
# inspired by https://www.youtube.com/watch?v=NZde8Xt78Iw

import cv2
import mediapipe as mp
import numpy as np
import time # check framerate

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        # formality to use mp mod -> initializes mp hand object
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    # draw hand
    def findHands(self, img, draw=True):
      
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # hands only use RGB images
        self.results = self.hands.process(imgRGB)
        # print(self.results.multi_hand_landmarks) # checks hand positions

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # draw hands if you want it to draw
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) # draws a single hand and connections btw finfers
        return img
        
    # find position of landmarks
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []

        # get specific hand
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark): # get index of finger landmark
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id,cx,cy) # print id of landmark and position on screen
                lmList.append([id, cx, cy])
                
                #if id == 1: # emphasizes which landmark is tracked
                if draw:
                    # can change size, color
                    cv2.circle(img, (cx,cy), 15, (255, 0 ,255), cv2.FILLED)
        return lmList


def main():
    prevTime = 0
    # open camera
    cap = cv2.VideoCapture(0) # can change to 1

    # initialize detector class
    detector = handDetector()

    while True:
        # get image
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) != 0: # if landmark on screen
            print(lmList[4]) # int based on which landmark you want -> prints pos of that landmark

        currTime = time.time()
        fps = 1/(currTime-prevTime)
        prevTime = currTime
        cv2.putText(img, "Draw here!", (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow("Latte art!", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()

# """
# Hand Tracing Module
# By: Murtaza Hassan
# Youtube: http://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
# Website: https://www.computervision.zone
# """

# import cv2
# import mediapipe as mp
# import time


# class handDetector():
#     def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.modelComplexity = modelComplexity
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon

#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)

#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms,
#                                                self.mpHands.HAND_CONNECTIONS)
#         return img

#     def findPosition(self, img, handNo=0, draw=True):

#         lmList = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             for id, lm in enumerate(myHand.landmark):
#                 # print(id, lm)
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 # print(id, cx, cy)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

#         return lmList


# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(0)
#     detector = handDetector()
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])

#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime

#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                     (255, 0, 255), 3)

#         cv2.imshow("Image", img)
#         cv2.waitKey(1)


# if __name__ == "__main__":
#     main()