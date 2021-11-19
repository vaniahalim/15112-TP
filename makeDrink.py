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
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    canvas.create_image(app.width*0.1, app.height*0.92, image=app.leftArrowImg)

    # drink options
    canvas.create_image(app.width/2+10, app.height/2+20, image=app.cup)
    canvas.create_image(app.width * (0.1), app.height * 0.15, image=app.espresso.img)
    canvas.create_image(app.width * (0.1), app.height * 0.30, image=app.dairy.img)
    canvas.create_image(app.width * (0.1), app.height * 0.45, image=app.oat.img)
    canvas.create_image(app.width * (0.1), app.height * 0.60, image=app.soy.img)
    canvas.create_image(app.width * (0.1), app.height * 0.75, image=app.almond.img)
    canvas.create_oval(app.width/2-app.currBase.r, app.height/2-app.currBase.r, app.width/2+app.currBase.r, app.height/2+app.currBase.r, fill=app.currBase.color)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
# convert hex values to RGB
def hexToRgb(hex):
    hex = str(hex[1:])
    red = int(hex[:2], 16)
    green = int(hex[2:4], 16)
    blue = int(hex[4:6], 16)
    return red, green, blue

# SOURCE: https://www.educative.io/edpresso/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python
# combines colors and converts to hex value
def combineColors(app, base1, base2):
    r1, g1, b1 = hexToRgb(base1.color)
    r2, g2, b2 = hexToRgb(base2.color)
    r3 = int((r1 * base1.r + r2 * base2.r) / (base1.r + base2.r))
    g3 = int((g1 * base1.r + g2 * base2.r) / (base1.r + base2.r))
    b3 = int((b1 * base1.r + b2 * base2.r) / (base1.r + base2.r))
    return ('#{:02X}{:02X}{:02X}').format(r3, g3, b3)

def makeDrinkMode_mousePressed(app, event):
    x = event.x
    y = event.y
   
    print(app.currBase.name)
    print(app.currBase.r)

    # select bases
    if distance(x, y, app.width * (0.1), app.height * 0.15) < 37:
        if not app.cupFull:
            app.espresso.r += 10
            app.currBase.color = combineColors(app, app.currBase, app.espresso)
            app.currBase.r += 10
        if app.currBase.r == 140:
            app.cupFull = True
        
    elif distance(x, y, app.width * (0.1), app.height * 0.30) < 37:
        if not app.cupFull:
            app.dairy.r += 10
            app.currBase.color = combineColors(app, app.currBase, app.dairy)
            app.currBase.r += 10
        if app.currBase.r == 140:
            app.cupFull = True

    elif distance(x, y, app.width * (0.1), app.height * 0.45) < 37 :
        if not app.cupFull:
            app.oat.r += 10
            app.currBase.color = combineColors(app, app.currBase, app.oat)
            app.currBase.r += 10
        if app.currBase.r == 140:
            app.cupFull = True

    elif distance(x, y, app.width * (0.1), app.height * 0.60) < 37:
        if not app.cupFull:
            app.soy.r += 10
            app.currBase.color = combineColors(app, app.currBase, app.soy)
            app.currBase.r += 10
        if app.currBase.r == 140:
            app.cupFull = True
            
    elif distance(x, y, app.width * (0.1), app.height * 0.75) < 37:
        if not app.cupFull:
            app.almond.r += 10
            app.currBase.color = combineColors(app, app.currBase, app.almond)
            app.currBase.r += 10
        if app.currBase.r == 140:
            app.cupFull = True

    # button to go to latte art page
    elif distance(x, y, app.width*0.92, app.height*0.92) < 30:
        app.mode = "latteArtMode"
    # button to go to cafe page
    elif distance(x, y, app.width*0.1, app.height*0.92) < 30:
        app.mode = "cafeMode"

def makeDrinkMode_keyPressed(app, event):
    pass





