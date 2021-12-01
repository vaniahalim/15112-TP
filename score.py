# SCREEN: scores drink based on correct bases, correct base proportions, art similarity

# SOURCES
# ssim: https://abndistro.com/post/2019/07/07/detecting-image-differences-using-python-and-opencv/#compute-structural-similarity-index-between-images-and-obtain-difference-image
# cup point: https://www.flaticon.com/premium-icon/coffee_2608044?term=happy%20coffe&page=1&position=1&page=1&position=1&related_id=2608044&origin=search
# star: https://www.flaticon.com/free-icon/star_1828884?term=star&page=1&position=7&page=1&position=7&related_id=1828884&origin=search#
# leaf: https://www.flaticon.com/premium-icon/palm_3086264?term=leaf&page=1&position=13&page=1&position=13&related_id=3086264&origin=search
# heart: https://www.flaticon.com/free-icon/like_535234?term=heart&page=1&position=10&page=1&position=10&related_id=535234&origin=search

from cmu_112_graphics_openCV import *
from classes import *
from tkinter import *
from skimage.metrics import structural_similarity

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''

def scoreMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "peachpuff")
    canvas.create_text(app.width/2, app.height/10, text="Judging...", font="Baskerville 24")
    canvas.create_image(app.width*0.9, app.height*0.92, image=app.rightArrowImg)
    
    # displays result of player's drawing
    canvas.create_image(app.width*0.75, app.height*0.4, image=app.resultImg)
    # displays customer desired art
    canvas.create_rectangle(app.width*0.25-100, app.height*0.4-100, app.width*0.25+100, app.height*0.4+100, fill=app.currBase.color, width=0)
    canvas.create_image(app.width*0.25, app.height*0.4, image=app.artOrdered)

    # score rubrics
    canvas.create_image(605, 35, image=app.helpImg)
    # text 
    canvas.create_text(app.width/4, app.height*0.2, text="Customer Order")
    canvas.create_text(app.width*0.75, app.height*0.2, text="Your creation")
    # customer order
    if app.currCustomer.drink in ["Latte", "Cappucino","Macchiato", "Cortado"]:
        flav = "espresso"
    if app.currCustomer.drink == "Matcha":
        flav = "matcha"
    if app.currCustomer.drink == "Mocha":
        flav = "mocha"
    if app.currCustomer.drink == "Chai":
        flav = "chai"
    if app.currCustomer.drink in ["Macchiato", "Cortado"]:
        canvas.create_text(app.width/4, app.height*0.6, text=f"Ingredients... {flav}, foam")
    else:
        canvas.create_text(app.width/4, app.height*0.6, text=f"Ingredients... {flav}, {app.currCustomer.base}, foam")
    canvas.create_text(app.width/4, app.height*0.65, text=f"Proportions...{app.drinkOrder}")
    # player creation
    canvas.create_text(app.width*0.75, app.height*0.6, text=f"{getIngredients(app, app.drinkMade)}")
    canvas.create_text(app.width*0.75, app.height*0.65, text=f"{app.drinkMade}")
    canvas.create_text(app.width/2, app.height*0.7, text=f"Art...{app.artScore}")

    # award cup scores for correct base and proportions
    if app.isCorrectBase:
        canvas.create_image(app.width*(1/3), app.height*0.8, image=app.cupScoreImg)
    if not app.isCorrectBase:
        canvas.create_image(app.width*(1/3), app.height*0.8, image=app.cupNoScoreImg)
    if app.isCorrectProportions:
        canvas.create_image(app.width*(1/2), app.height*0.8, image=app.cupScoreImg)
    if not app.isCorrectProportions:
        canvas.create_image(app.width*(1/2), app.height*0.8, image=app.cupNoScoreImg)
    if app.artScore >= 0.4:
        canvas.create_image(app.width*(2/3), app.height*0.8, image=app.cupScoreImg)
    if app.artScore < 0.4:
        canvas.create_image(app.width*(2/3), app.height*0.8, image=app.cupNoScoreImg)

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
# helper: checks if drink made contains the correct base
# drinkMade is a dictionary containing espresso + milk bases and their radii
# customer is app.currCustomer
def correctBase(drinkMade, customer):
    if customer.drink in ["Latte", "Cappucino","Macchiato", "Cortado"]:
        if "espresso" not in drinkMade: return False
    if customer.drink == "Matcha":
        if "matcha" not in drinkMade: return False
    if customer.drink == "Mocha":
        if "mocha" not in drinkMade: return False
    if customer.drink == "Chai":
        if "chai" not in drinkMade: return False
    if "foam" not in drinkMade: return False
    # more than 1 milk base
    if customer.drink in ["Macchiato", "Cortado"]:
        if len(drinkMade) != 2 : return False
    if customer.drink in ["Latte", "Cappucino", "Matcha", "Mocha", "Chai"]:
        if customer.base not in drinkMade: return False
        # wrong base
        if len(drinkMade) != 3 : return False
    return True

# helper: checks if drink made has the right proportion of espresso and milk and milk foam
def correctProportions(app, drinkMade, customer):
    latte = {"espresso": 30, customer.base: 110, "foam":10}
    macchiato = {"espresso": 70, "foam": 30}
    cappucino = {"espresso": 50, customer.base: 50, "foam": 50}
    cortado = {"espresso": 70, "foam": 60}
    matcha = {"matcha": 30, customer.base: 110, "foam":10}
    mocha = {"mocha": 30, customer.base: 110, "foam":10}
    chai = {"chai": 30, customer.base: 110, "foam":10}
    if customer.drink == "Latte":
        app.drinkOrder = latte
        if drinkMade != latte:
            return False
    if customer.drink == "Macchiato":
        app.drinkOrder = macchiato
        if drinkMade != macchiato:
            return False
    if customer.drink == "Cappucino":
        app.drinkOrder = cappucino
        if drinkMade != cappucino:
            return False
    if customer.drink == "Cortado":
        app.drinkOrder = cortado
        if drinkMade != cortado:
            return False
    if customer.drink == "Matcha":
        app.drinkOrder = matcha
        if drinkMade != matcha:
            return False
    if customer.drink == "Mocha":
        app.drinkOrder = mocha
        if drinkMade != mocha:
            return False
    if customer.drink == "Chai":
        app.drinkOrder = chai
        if drinkMade != chai:
            return False
    return True

# helper: scores art based on structural similarity
def artScoring(app):
    if app.currCustomer.art == "star":
        orderedArt = cv2.imread("images/star.png")
        app.artOrdered = app.starImg
    elif app.currCustomer.art == "heart":
        orderedArt = cv2.imread("images/heart.png")
        app.artOrdered = app.heartImg
    elif app.currCustomer.art == "flower":
        orderedArt = cv2.imread("images/flower.png")
        app.artOrdered = app.flowerImg

    resultArt = cv2.imread("result.jpg")

    # resize for faster processing
    orderedArt = cv2.resize(orderedArt, (200, 200))    
    resultArt = cv2.resize(resultArt, (200, 200))

    orderedArt = cv2.cvtColor(orderedArt, cv2.COLOR_BGR2GRAY)
    resultArt = cv2.cvtColor(resultArt, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(orderedArt, resultArt, full=True)
    formatted = "{:.2f}".format(score)
    return float(formatted)

# helper: get ingredients in drink
def getIngredients(app, drink):
    ingredients = list()
    for k in drink:
        ingredients.append(k)
    result = ", ".join(ingredients)
    return result

# helper: get proportions in drink
def getProportions(app):
    pass

def scoreMode_timerFired(app):
    app.resultImg = ImageTk.PhotoImage(app.loadImage("result.jpg"))
    app.disp_cam = False
    app.artScore = artScoring(app)
    
    if correctBase(app.drinkMade, app.currCustomer): 
        app.isCorrectBase = True
    if correctProportions(app, app.drinkMade, app.currCustomer):
        app.isCorrectProportions = True
    
    print(app.drinkMade)
    print(app.currCustomer.drink)
    print(app.currCustomer.base)
   
def scoreMode_mousePressed(app, event):
    x = event.x
    y = event.y

    # go to rubrics page
    if distance(x, y, 605, 35) < 30:
        app.mode = "scoreInstructionsMode"

    if distance(x, y, app.width*0.92, app.height*0.92) < 30:
        app.waiter.x = 395
        app.waiter.y = 395
        app.isServing = False
        app.activeChar = app.barista

        # increase score count
        if correctBase(app.drinkMade, app.currCustomer): 
            app.score += 1
        if correctProportions(app, app.drinkMade, app.currCustomer):
            app.score += 1
        if app.artScore >= app.scoreThresh:
            app.score += 1
        if app.score >= app.winScore:
            app.win = True

        # reset drink variables
        app.currBase = Base("empty", "#FFFFFF", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/coffebeans.png"),1/10)))
        app.cupFull = False
        app.drinkMade = dict()
        app.espresso.r = 0
        app.dairy.r = 0
        app.oat.r = 0
        app.soy.r = 0
        app.almond.r = 0
        app.matcha.r = 0
        app.mocha.r = 0
        app.chai.r = 0
        app.foam.r = 0
        app.mode = "cafeMode"
        
    
    