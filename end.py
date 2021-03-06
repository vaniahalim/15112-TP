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
    if app.win:
        canvas.create_image(app.width/2, app.height/2, image=app.passImg)
    elif not app.win:
        canvas.create_image(app.width/2, app.height/2, image=app.failImg)
        # show progress bar
        canvas.create_rectangle(app.width/2-100, app.height*0.5-15, app.width/2+100, app.height*0.5+15, fill="lightgrey", width=0.5)
        canvas.create_rectangle(app.width/2-100, app.height*0.5-15, app.width/2-100+(app.score/app.winScore)*200, app.height*0.5+15, fill="pink")
        canvas.create_text(app.width/2, app.height*0.5, text="Progress...")
    
    # go back to home page
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def endMode_mousePressed(app, event):
    x = event.x
    y = event.y
    if distance(x, y, app.width*0.92, app.height*0.92) < 30:
        app.mode = "homeMode"
        app.isStarting = True
        app.currCustomer = None
        app.isOrdering = False
        app.time = 0
        
        # update player progress if they passed level
        # SOURCE: https://www.kite.com/python/answers/how-to-edit-a-specific-line-in-a-text-file-in-python
        if app.win:
            f = open("users.txt", "r")
            lines = f.readlines()
            print(lines)
            for i in range(len(lines)):
                if app.username in lines[i]:
                    app.day += 1
                    lines[i] = f"{app.username} {app.day} \n"
                    print(lines[i])

            f = open("users.txt", "w")
            f.writelines(lines)
            f.close()
        