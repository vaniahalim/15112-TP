# SCREEN: scores drink based on correct bases, correct base proportions, art similarity

# SOURCES
# cup point: https://www.flaticon.com/premium-icon/coffee_2608044?term=happy%20coffe&page=1&position=1&page=1&position=1&related_id=2608044&origin=search

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
def scoreMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "peachpuff")
    canvas.create_text(app.width/2, app.height/10, text="Judging...", font="Baskerville 24")
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    canvas.create_image(app.width*0.1, app.height*0.92, image=app.leftArrowImg)
    canvas.create_image(app.width*0.75, app.height*0.4, image=app.imageToTk(app.imgCanvas))


    # coffee results
    # canvas.create_img(app.currCustomer.)

    # text 
    canvas.create_text(app.width/4, app.height*0.2, text="Customer Order")
    canvas.create_text(app.width*0.75, app.height*0.2, text="Your creation")
    canvas.create_text(app.width/3, app.height*0.7, text="Ingredients......")
    canvas.create_text(app.width/3, app.height*0.75, text="Proportions......")
    canvas.create_text(app.width/3, app.height*0.8, text="Art..............")

    # print scores
    
    if app.isCorrectBase:
        canvas.create_image(app.width*(2/3), app.height*0.6, image=app.cupScoreImg)
    if app.isCorrectProportions:
        canvas.create_image(app.width*(2/3), app.height*0.7, image=app.cupScoreImg)

# helper: draw customer order and your creation
# def drawDrink(app, canvas):


'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
# helper: checks if drink made contains the correct base
# drinkMade is a dictionary containing espresso + milk bases and their radii
# customer is app.currCustomer
def correctBase(drinkMade, customer):
    if "espresso" not in drinkMade: return False
    if "foam" not in drinkMade: return False
    # more than 1 milk base
    if customer.drink in ["Macchiato", "Cortado"]:
        if len(drinkMade) != 2 : return False
    if customer.drink in ["Latte", "Cappucino"]:
        if len(drinkMade) != 3 : return False
    # wrong base
    if customer.base not in drinkMade: return False

# helper: checks if drink made has the right proportion of espresso and milk and milk foam
def correctProportions(drinkMade, customer):
    latte = {"espresso": 30, customer.base: 110, "foam":10}
    macchiato = {"espresso": 30, "foam": 10}
    cappucino = {"espresso": 30, customer.base: 30, "foam": 30}
    cortado = {"espresso": 30, "foam": 30}
    if customer.drink == "Latte":
        if drinkMade != latte:
            return False
    if customer.drink == "Macchiato":
        if drinkMade != macchiato:
            return False
    if customer.drink == "Cappucino":
        if drinkMade != cappucino:
            return False
    if customer.drink == "Cortado":
        if drinkMade != cortado:
            return False
    
def scoreMode_timerFired(app):
    app.disp_cam = False
    if correctBase(app.drinkMade, app.currCustomer): 
        app.isCorrectBase = True
        app.score += 1
    if correctProportions(app.drinkMade, app.currCustomer):
        app.isCorrectProportions = True
        app.score += 1