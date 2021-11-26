# SCREEN: homeMode
# TO ADD: tkentry to get user input

# import modules
from cmu_112_graphics_openCV import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def homeMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, image=app.homeImg)
    canvas.create_text(app.width*0.25, app.height*0.11, text=f"It's day {app.day}!", font="Arial 28 bold", fill="#481C0A")
    # canvas.create_window(app.width/2, app.height/1.2, width= 300, window=app.selectUser)
'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def homeMode_mousePressed(app, event):
    x = event.x
    y = event.y
   
    if (x >= app.width/2-app.width/5 and x <= app.width/2+app.width/5) and \
    (y >= app.height*0.87-29 and y <= app.height*0.87+29):
        app.mode = 'cafeMode'

def homeMode_keyPressed(app, event):
    if event.key == "Return" or event.key == "Enter":
        app.mode = "cafeMode"
        # check if username is in app.usernames list, if not create a new user
        app.user = app.selectUser.get()
        print("entered")

