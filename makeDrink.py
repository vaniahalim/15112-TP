# SCREEN: makeDrinkMode
# SOURCES:
# button: https://www.customicondesign.com/free-icons/flat-cute-icon-set/flat-cute-icon-set-part-arrow/
# coffee cup: https://www.istockphoto.com/photos/empty-coffee-cup-top-view
# coffee beans: "https://www.flaticon.com/premium-icon/coffee-beans_3219333?term=coffee%20bean&page=1&position=13&page=1&position=13&related_id=3219333&origin=search"
# dairy milk: https://www.flaticon.com/authors/amonrat-rungreangfangsai"
# oat milk: "https://www.flaticon.com/premium-icon/oats_3982829?term=oats&page=1&position=6&page=1&position=6&related_id=3982829&origin=search"
# soy milk: "https://www.flaticon.com/premium-icon/soy-milk_3414349?term=soy%20milk&related_id=3414349"
# almond milk: " https://www.flaticon.com/premium-icon/almond-milk_3414348?term=almond%20milk&page=1&position=48&page=1&position=48&related_id=3414348&origin=search"

# import modules
from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def makeDrinkMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "lavender")
    canvas.create_text(app.width/2, app.height/10, text="Choose a flavour", font="Baskerville 24")
    canvas.create_image(app.width*0.9, app.height*0.9, image=app.rightArrowImg)

    # drink options
    canvas.create_image(app.width/2+10, app.height/2+20, image=app.cup)
    canvas.create_image(app.width * (0.1), app.height * 0.15, image=app.espresso.img)
    canvas.create_image(app.width * (0.1), app.height * 0.30, image=app.dairy.img)
    canvas.create_image(app.width * (0.1), app.height * 0.45, image=app.oat.img)
    canvas.create_image(app.width * (0.1), app.height * 0.60, image=app.soy.img)
    canvas.create_image(app.width * (0.1), app.height * 0.75, image=app.almond.img)
    if app.currBase != None:
        canvas.create_oval(app.width/2-app.currBase.r, app.height/2-app.currBase.r, app.width/2+app.currBase.r, app.height/2+app.currBase.r, fill=app.currBase.color)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def makeDrinkMode_mousePressed(app, event):
    x = event.x
    y = event.y
    if app.currBase != None:
        print(app.currBase.name)
        print(app.currBase.r)

    # select bases
    if distance(x, y, app.width * (0.1), app.height * 0.15) < 37:
        app.currBase = app.espresso
        while app.currBase.r < 140:
            app.currBase.r += 10
    elif distance(x, y, app.width * (0.1), app.height * 0.30) < 37:
        app.currBase.r = app.dairy
        while app.currBase < 140:
            app.currBase.r += 10
    elif distance(x, y, app.width * (0.1), app.height * 0.45) < 37 :
        app.currBase = app.oat
    elif distance(x, y, app.width * (0.1), app.height * 0.60) < 37:
        app.currBase = app.soy
    elif distance(x, y, app.width * (0.1), app.height * 0.75) < 37:
        app.currBase = app.almond
    # button to go to latte art page
    elif distance(x, y, app.width*0.9, app.height*0.9) < 30:
        app.mode = "latteArtMode"

def makeDrinkMode_keyPressed(app, event):
    pass





