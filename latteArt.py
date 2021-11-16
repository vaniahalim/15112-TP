# SCREEN: draw latte art
# SOURCES:
# button: https://www.customicondesign.com/free-icons/flat-cute-icon-set/flat-cute-icon-set-part-arrow/

# import modules
from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def latteArtMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lavender")
    canvas.create_text(app.width/2, app.height/10, text="Time for latte art!", font="Baskerville 24")
    canvas.create_image(app.width*0.9, app.height*0.9, image=app.rightArrowImg)

    app.drawCamera(canvas)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def latteArtMode_mousePressed(app, event):
    x = event.x
    y = event.y

    if distance(x, y, app.width*0.9, app.height*0.9) < 30:
        app.mode = "latteArtMode"

def latteArtMode_cameraFired(app):
    app.cameraOpen = True
    

def latteArtMode_keyPressed(app, event):
    if event.key == "q":
        App._theRoot.app.quit()
