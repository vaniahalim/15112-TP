# main file to run animation
# import all files
from cmu_112_graphics_openCV import *
from classes import *
from home import *
from cafe import *
from makeDrink import *
from latteArt import *
from score import *
from end import *
import tkinter as tk
import pickle
import random

# def user class
'''''''''''''''''''''''''''''''''
MODEL
'''''''''''''''''''''''''''''''''
def appStarted(app):
    app.username = ""
    app.selectUser = tk.Entry()
    app.counter = 0
    app.day = 1

    app.mode = 'homeMode'
    print(app.mode)
    app.cameraOpen = False
    app.disp_cam = False
    
    # cafe grid layout
    app.rows, app.cols, app.cellSize, app.margin = cafeDimensions()
    app.emptyColor = "pink"
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]
    app.boardGrid = [([0] * app.cols) for row in range(app.rows)]
    app.score = 0
    app.winScore = 10
    app.win = False
    app.time = 0
    app.timeOver = False

    # miscellaneous
    app.rightArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/rightarrow.png"), 1/2))
    app.leftArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/leftarrow.png"), 1/2))
    app.timerImg = ImageTk.PhotoImage(app.loadImage("images/timer.jpg"))
    app.moonImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/moon.png"),1/12))
    app.sunImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/sun.png"),1/12))

    # furniture
    cofMacImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cofmac.png"),1/10))
    app.cofMac = Furniture("cofMac", 495, 245, cofMacImg)
    app.boardGrid[getRow(app, app.cofMac.y)][getCol(app, app.cofMac.x)] = 1
    tableImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/table.png"),1/10))
    app.table = Furniture("table", 95+50*random.randint(0, 4), 95+50*random.randint(2, 8), tableImg)
    # app.furniture = [cofMac]
   
    # characters
    baristaImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/barista.png"),1/10))
    app.barista = Character("barista", 395 , 145, baristaImg)
    waiterImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/waiter.png"),1/8))
    app.waiter = Character("waiter", 395, 395, waiterImg)
    app.activeChar = app.barista

    # customers
    girl1Img = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/girl1.png"),1/4))
    girl2Img = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/girl2.png"),1/4))
    boy1Img = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/boy1.png"),1/4))
    boy2Img = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/boy2.png"),1/4))

    app.custImgs = [girl1Img, girl2Img, boy1Img, boy2Img]
    app.customers = []
    app.currCustomer = None
    app.isEntering = False
    app.isOrdering = False
    app.isWaiting = False
    app.isServing = False
    app.path = []

    # orders
    app.cup = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/topviewcup.png"), 0.9))
    app.drinks = ['Latte', 'Macchiato', 'Cappucino', 'Cortado']
    app.espresso = Base("espresso", "#481C0A", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/coffebeans.png"),1/10)))
    app.dairy = Base("dairy", "#F6F1EF", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/dairymilk.png"),1/10)))
    app.oat = Base("oat", "#F2E8D4", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/oatmilk.png"),1/10)))
    app.soy = Base("soy", "#F2E8D4", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/soymilk.png"),1/10)))
    app.almond = Base("almond", "#F2E8D4", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/almondmilk.png"),1/10)))
    app.bases = ["espresso", "dairy", "oat", "soy", "almond"]
    app.currBase = Base("empty", "#FFFFFF", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/coffebeans.png"),1/10)))
    app.foam = Base("foam", "#FFFFFF", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/steamer.png"),1/10)))
    app.arts = ['heart', 'star', 'flower']
    app.currOrder = dict()
    app.drinkMade = dict()
    app.drinkOrder = ""
    app.cupFull = False
    app.resultImg = ""
    # app.flavors

    # openCV
    app.imgCanvas = np.zeros((200,200,3), np.uint8)
    
    # scoring
    app.isCorrectBase = False
    app.isCorrectProportions = False
    app.artScore = 0
    app.cupScoreImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cupscore.png"), 1/8))
    app.cupNoScoreImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cupnoscore.png"), 1/8))
    app.heartImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/heart.png"), 1/4))
    app.starImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/star.png"), 1/4))
    app.flowerImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/flower.png"), 1/4))
    app.artOrdered = ""

    # end
    app.closedImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/close.png"), 1/3.5))


    # loading and saving into username
    # app.user = User()
    # app.users = []

    # pickled module: loading user data from file
    # check if file exists, if not create new file
    # with open(f"{app.username}_progress.pkl", "rb") as inp:
    #     app.user = pickle.load(inp)
    


'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def timerFired(app):
    # with open(f"{app.username}.pkl", "wb") as outp:
    #     pickle.dump(app.user, outp, -1)
    if app.time == 400: 
        app.timeOver
        app.mode = "endMode"
        app.day += 1
  

runApp(width = 640, height = 640)
# print(combineColors(app, "#481C0A", "#481C0A"))

# app started: load
# timer fired: pickle.dump