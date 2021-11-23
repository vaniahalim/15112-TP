# SCREEN: displays when the day is over

# SOURCES:
# closed sign: https://www.flaticon.com/premium-icon/close_2169997?term=closed%20sign&page=1&position=12&page=1&position=12&related_id=2169997&origin=search

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def endMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "peachpuff")
    canvas.create_image(app.width/2, app.height*0.1, image=app.closedImg)
    if app.win:
        canvas.create_text(app.width/2, app.height*0.25, text="Lovely! You did it!", font="Baskerville 22")
    elif not app.win:
        canvas.create_text(app.width/2, app.height*0.25, text="Aww... try again!", font="Baskerville 22")
    
    # show progress bar
    canvas.create_rectangle(app.width/2-100, app.height*0.4-15, app.width/2+100, app.height*0.4+15, fill="lightgrey", width=0.5)
    canvas.create_rectangle(app.width/2-100, app.height*0.4-15, app.width/2-100+(app.score/app.winScore)*200, app.height*0.4+15, fill="pink")
    canvas.create_text(app.width/2, app.height*0.4, text="Progress...")
    
    # go back to home page
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    #canvas.create_image(app.width*0.1, app.height*0.92, image=app.leftArrowImg)


'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def endMode_mousePressed(app, event):
    x = event.x
    y = event.y
    if distance(x, y, app.width*0.92, app.height*0.92) < 30:
        app.mode = "homeMode"
        app.day += 1
        app.isStarting = True
        app.currCustomer = None
        app.time = 0
        print(app.day)