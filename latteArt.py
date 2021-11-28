# SCREEN: draw latte art
# SOURCES: 
# latte art: https://www.youtube.com/watch?v=NZde8Xt78Iw
# button: https://www.customicondesign.com/free-icons/flat-cute-icon-set/flat-cute-icon-set-part-arrow/

# import modules
from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *
from makeDrink import hexToRgb
from handTrackingMod import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def latteArtMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lavender")
    canvas.create_text(app.width/2, app.height/10, text="Time for latte art!", font="{Arial Rounded MT Bold} 24")
    canvas.create_text(app.width/2, app.height*0.15, text="Press c to open the camera! Move it beside the game screen", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.2, text="Use index finger to pour the foam; Raise 2 or more fingers to stop", font="Avenir 16")
    canvas.create_text(app.width/2, app.height*0.85, text="Tip: work inside the black circle and pour slowly...", font="Avenir 16")
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    canvas.create_image(app.width/2+10, app.height/2+20, image=app.cup)
    canvas.create_oval(app.width/2-app.currBase.r, app.height/2-app.currBase.r, app.width/2+app.currBase.r, app.height/2+app.currBase.r, fill=app.currBase.color, width=0)
    # show camera
    if app.disp_cam:
        resized = cv2.resize(app.frame, (640,360))
        cv2.imshow('Camera', resized)
        canvas.create_image(app.width/2, app.height/2, image=app.imageToTk(app.imgCanvas))

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''

def latteArtMode_mousePressed(app, event):
    x = event.x
    y = event.y
    
    if distance(x, y, app.width*0.9, app.height*0.92) < 30:
        app.mode = "cafeMode"
        app.isServing = True
        app.activeChar = app.waiter
        app.barista.x, app.barista.y = (395, 195)
        app.waiter.x, app.waiter.y = (395, 395)
        app.disp_cam = False
      
   
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
 
    # import image
    img = app.frame
    # find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,0) # get landmark positions

    if len(lmList) != 0: # if landmark on screen
        x_index, y_index = lmList[8][1:] # x,y coordinates of finger
        x_mid, y_mid = lmList[12][1:]

        # check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers) # list of which fingers are up

        # selection mode: 2 fingers are up
        if fingers[1] == 1 and fingers[2] == 1:
            x_prev, yprev = 0, 0 # reset position of finger everytime you select

        # drawing mode: index finger is up
        if fingers[1]==1 and fingers[2] == 0:
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
    
    #save file
    cv2.imwrite("result.jpg", app.imgCanvas)
 
def latteArtMode_keyPressed(app, event):
    if event.key == "c":
        app.imgCanvas = np.zeros((200,200,4), np.uint8) 
        a,b,c = hexToRgb(app.currBase.color)
        # change color of canvas to match drink color
        app.imgCanvas[:,:] = [c, b, a, 0]
        app.disp_cam = True

def latteArtMode_timerFired(app):
    if app.time >= app.gameTime: 
        app.timeOver
        app.mode = "endMode"
    app.time += 1
