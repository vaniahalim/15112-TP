# SCREEN: display scoring rubrics

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def scoreInstructionsMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lemon chiffon")
    canvas.create_text(app.width/2, app.height/10, text="Scoring Rubrics", font="Baskerville 24")
    
    canvas.create_text(app.width/2, app.height*0.15, text="Your drink is scored based on Ingredients + Proportions + Art", font="Avenir 18")
    canvas.create_image(app.width*(0.4), app.height*0.25, image=app.cupScoreImg)
    canvas.create_text(app.width*0.4, app.height*0.35, text="Cup Point! :)", font="Avenir 16")
    canvas.create_image(app.width*(0.6), app.height*0.25, image=app.cupNoScoreImg)
    canvas.create_text(app.width*0.6, app.height*0.35, text="No Cup Point! :(", font="Avenir 16")
    canvas.create_text(app.width/2, app.height*0.45, text="You get a Cup Point for pouring in the right ingredients", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.5, text="You get a Cup Point for pouring them in the right proportions", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.55, text="You get a Cup Point if your art score > the score threshold", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.6, text="The score threshold is determined by your game performance", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.7, text="Cup Points increase your progress", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.75, text="Reach the target to start the next day", font="Avenir 18")
    canvas.create_text(app.width/2, app.height*0.85, text="Current progress:", font="Avenir 18")
    canvas.create_rectangle(app.width/2 - 100, 561, app.width/2 + 100, 591, fill="lightgrey", width=0.5)
    if not app.win and not app.timeOver:
        canvas.create_rectangle(app.width/2 - 100,561, app.width/2-100+(app.score/app.winScore)*200, 591, fill="pink")
    canvas.create_text(app.width/2, 576, text="Progress...")
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
    