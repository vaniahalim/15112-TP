# SCREEN: menu page
# SOURCES:
# background created by me on Canvas
# empty coffee cup image:https://favpng.com/png_view/coffee-coffee-cup-mug-drawing-teacup-png/g2fp2fAn

from cmu_112_graphics_openCV import *
from classes import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def menuMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.menuImg)
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)

def menuMode_mousePressed(app, event):
    x = event.x
    y = event.y
    if distance(x, y, app.width*0.92, app.height*0.92) < 30:
        app.mode = "cafeMode"

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def menuMode_timerFired(app):
    app.time += 1

