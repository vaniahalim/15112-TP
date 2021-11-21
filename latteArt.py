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
    canvas.create_image(app.width/2, app.height/2, image=app.imageToTk(app.imgCanvas))

    # show camera
    if app.disp_cam:
        resized = cv2.resize(app.frame, (640,360))
        cv2.imshow('Camera', resized)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''

def latteArtMode_mousePressed(app, event):
    x = event.x
    y = event.y
    print(distance(x, y, app.width*0.1, app.height*0.92))
    if distance(x, y, app.width*0.1, app.height*0.92) < 30:
       app.mode = "makeDrinkMode"
    elif distance(x, y, app.width*0.9, app.height*0.92) < 30:
       app.mode = "scoreMode"
   
def latteArtMode_cameraFired(app):
    # mirror image
    app.frame = cv2.flip(app.frame, 1)
    # painter config
    drawColor = ()
    brushThickness = 15

    # open camera
    # change resolution
    app.camera.set(3, 1280) 
    app.camera.set(4, 720)  

    # initialize detector class
    detector = handDetector(detectionCon = 0.8)
    # initialize starting location
    x_prev, y_prev = 0, 0
    # draw on canvas instead of camera screen
   
    # import image

    img = app.frame
    # find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,0) # get landmark positions

    if len(lmList) != 0: # if landmark on screen
        x_index, y_index = lmList[8][1:] # x,y coordinates of finger
        print(lmList[8][1:])
        x_mid, y_mid = lmList[12][1:]

        # check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers) # list of which fingers are up

        # selection mode: 2 fingers are up
        if fingers[1] == 1 and fingers[2] == 1:
            x_prev, yprev = 0, 0 # reset position of finger everytime you select
        
            print("stop!")
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
            cv2.line(app.imgCanvas, (x_prev-540, y_prev-260), (x_index-540, y_index-260), drawColor, brushThickness) # draws onto a separate canvas created
    
        x_prev, y_prev = x_index, y_index # keep updating position of fingers

    cv2.putText(img, "Draw here!", (30,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.circle(img, (640, 360), 300, (0, 0, 0), 2)
    print
    
    # remove prev picture
    # try: 
    #     os.remove("Player drawing.jpg")
    # except: 
    #     pass

    # cv2.imshow("Latte art!", img)
    # cv2.imshow("Canvas", imgCanvas) # show canvas of drawing
    
    #save file
    # cv2.imwrite("Player drawing.jpg", imgCanvas)
    cv2.waitKey(1) # 0 gives still images
    
def latteArtMode_keyPressed(app, event):
    if event.key == "c":
        app.disp_cam = True
        app.imgCanvas = np.zeros((200,200,3), np.uint8) # canvas needs to happen in 112 graphics
    if event.key == "q":
        # App._theRoot.app.quit()
        app.disp_cam = False


