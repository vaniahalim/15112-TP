# SCREEN: display scoring rubrics

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def scoreInstructionsMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.scoreInsImg)
    canvas.create_image(app.width*(0.4), app.height*0.3, image=app.cupScoreImg)
    canvas.create_text(app.width*0.4, app.height*0.37, text="Cup Point! :)", font="Avenir 16")
    canvas.create_image(app.width*(0.6), app.height*0.3, image=app.cupNoScoreImg)
    canvas.create_text(app.width*0.6, app.height*0.37, text="No Cup Point! :(", font="Avenir 16")
    canvas.create_rectangle(app.width/2 - 100, 531, app.width/2 + 100, 561, fill="lightgrey", width=0.5)
    if not app.win and not app.timeOver:
        canvas.create_rectangle(app.width/2 - 100,531, app.width/2-100+(app.score/app.winScore)*200, 561, fill="pink")
    canvas.create_text(app.width/2, 546, text="Progress...")
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def scoreInstructionsMode_mousePressed(app, event):
    # button to go to cafe page
    x = event.x
    y = event.y
    
    if distance(x, y, app.width*0.9, app.height*0.92) < 30:
        app.mode = "scoreMode"
    