# SCREEN: display instructions of how to move in cafe

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def cafeInstructionsMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lemon chiffon")
    canvas.create_text(app.width/2, app.height/10, text="Instructions", font="Baskerville 24")
    
    canvas.create_text(app.width/2, app.height*0.2, text="Press Space to take orders from customers", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.25, text="Use arrow keys to move the Barista", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.3, text="To start making drinks, move to the Coffee Machine and press Enter", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.35, text="To check the menu, move to the Menu and press Enter", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.45, text="After creating your drink, you will play as the Waiter to serve it", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.5, text="Follow the green dots to reach the customer fastest", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.6, text="Game ends when La Barista closes at the end of the day", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.65, text="Earn Cup Points to make progress before La Barista closes", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.7, text="Reach the target to start the next day", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.8, text="Have fun! :)", font="Avenir 18")
    
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
    