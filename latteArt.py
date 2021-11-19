# SCREEN: draw latte art
# SOURCES: https://www.youtube.com/watch?v=NZde8Xt78Iw
# button: https://www.customicondesign.com/free-icons/flat-cute-icon-set/flat-cute-icon-set-part-arrow/

# import modules
from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *
# from latte_drawing_copy import *
from handTrackingMod import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def latteArtMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lavender")
    canvas.create_text(app.width/2, app.height/10, text="Time for latte art!", font="Baskerville 24")
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    canvas.create_image(app.width*0.1, app.height*0.92, image=app.leftArrowImg)
    canvas.create_image(app.width/2+10, app.height/2+20, image=app.cup)
    canvas.create_oval(app.width/2-app.currBase.r, app.height/2-app.currBase.r, app.width/2+app.currBase.r, app.height/2+app.currBase.r, fill=app.currBase.color)
    # suggested func to render drawing onto coffee
    if app.drawing != None:
        canvas.create_image(app.width/2+10, app.height/2+20, Image=app.drawing)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def latteArtMode_mousePressed(app, event):
    x = event.x
    y = event.y
    print(distance(x, y, app.width*0.1, app.height*0.92))
    if distance(x, y, app.width*0.1, app.height*0.92) < 30:
       app.mode = "makeDrinkMode"
   
def latteArtMode_cameraFired(app):
    # suggested func
    # app.vid = cap
    
    drawColor = ()

    # painter config
    brushThickness = 15

    # open camera
    cap = cv2.VideoCapture(0) 
    # change size of camera screen
    cap.set(3, 640) # width
    cap.set(4, 640)  #height

    # initialize detector class
    detector = handDetector(detectionCon = 0.8)
    # initialize starting location
    x_prev, y_prev = 0, 0
    # draw on canvas instead of camera screen
    imgCanvas = np.zeros((720,1280,3), np.uint8) # canvas needs to happen in 112 graphics

    while True:
        # import image
        success, img = cap.read() # get video
        img = cv2.flip(img, 1) # mirror image

        # find hand landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img,0) # get landmark positions

        if len(lmList) != 0: # if landmark on screen
            print(lmList[8]) # int based on which landmark you want -> prints pos of that landmark
            print(lmList[8][1:])
            x_index, y_index = lmList[8][1:] # x,y coordinates of finger
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

                cv2.line(img, (x_prev, y_prev), (x_index, y_index), drawColor, brushThickness) # camera detection
                app.drawing = cv2.line(imgCanvas, (x_prev, y_prev), (x_index, y_index), drawColor, brushThickness) # draws onto a separate canvas created
        
            x_prev, y_prev = x_index, y_index # keep updating position of fingers

        cv2.putText(img, "Draw here!", (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        
        # remove prev picture
        # try: 
        #     os.remove("Player drawing.jpg")
        # except: 
        #     pass

        cv2.imshow("Latte art!", img)
        # cv2.imshow("Canvas", imgCanvas) # show canvas of drawing
        
        #save file
        # cv2.imwrite("Player drawing.jpg", imgCanvas)
        cv2.waitKey(1) # 0 gives still images
    
def latteArtMode_keyPressed(app, event):
    if event.key == "q":
        App._theRoot.app.quit()


