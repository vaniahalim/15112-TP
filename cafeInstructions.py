# SCREEN: display instructions of how to move in cafe

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def cafeInstructionsMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.insImg)
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def cafeInstructionsMode_mousePressed(app, event):
    # button to go to cafe page
    x = event.x
    y = event.y
    
    if distance(x, y, app.width*0.9, app.height*0.92) < 30:
        app.mode = "cafeMode"
    