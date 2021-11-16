# SCREEN: homeMode
# TO ADD: tkentry to get user input

# import modules
from cmu_112_graphics_openCV import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def homeMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "pink")
    canvas.create_text(app.width/2, app.height/2, text="La Barista", font="Baskerville 48")
    canvas.create_rectangle(app.width/2-app.width/5, app.height/1.5-app.height/20, app.width/2+app.width/5, app.height/1.5+app.height/20, fill='lightblue')
    canvas.create_text(app.width/2, app.height/1.5, text="PLAY", font="Avenir 28" )
    canvas.create_window(app.width/2, app.height/1.2, width= 300, window=app.selectUser)
'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def homeMode_mousePressed(app, event):
    x = event.x
    y = event.y
   
    if (x >= app.width/2-app.width/5 and x <= app.width/2+app.width/5) and \
    (y >= app.height/1.5-app.height/20 and y <= app.height/1.5+app.height/20):
        app.mode = 'cafeMode'

def homeMode_keyPressed(app, event):
    if event.key == "Return" or event.key == "Enter":
        app.mode = "cafeMode"
        # check if username is in app.usernames list, if not create a new user
        app.user = app.selectUser.get()
        print("entered")




