# main file to run animation
# import all files
from cmu_112_graphics_openCV import *
from classes import *
from home import *
from cafe import *
from makeDrink import *
from latteArt import *
from score import *
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

    app.mode = 'cafeMode'
    print(app.mode)
    app.cameraOpen = False
    app.disp_cam = False
    
    # cafe grid layout
    app.rows, app.cols, app.cellSize, app.margin = cafeDimensions()
    app.margin = 20
    app.emptyColor = "pink"
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]

    # furniture
    cofMacImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cofmac.png"),1/10))
    app.cofMac = Furniture("cofMac", 495, 245, cofMacImg)
    app.board[getRow(app, app.cofMac.y)][getCol(app, app.cofMac.x)] = "blue"

    tableImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/table.png"),1/10))
    app.table = Furniture("table", random.randint(70, 170), random.randint(320, 520), tableImg)
    # app.furniture = [cofMac]
   
    # characters
    baristaImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/barista.png"),1/10))
    app.barista = Character("barista", 370 , 120, baristaImg)
    waiterImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/waiter.png"),1/8))
    app.waiter = Character("waiter", 370, 370, waiterImg)
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
    app.cupFull = False
    # app.flavors

    # miscellaneous
    app.rightArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/rightarrow.png"), 1/2))
    app.leftArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/leftarrow.png"), 1/2))
    app.clockTimer = []
    app.progressbar = []

    # openCV
    app.imgCanvas = np.zeros((200,200,3), np.uint8)

    # scoring
    app.isCorrectBase = False
    app.isCorrectProportions = False
    app.score = 0
    app.cupScoreImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cupscore.png"), 1/8))

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
# def timerFired(app):
    # with open(f"{app.username}.pkl", "wb") as outp:
    #     pickle.dump(app.user, outp, -1)
  

runApp(width = 640, height = 640)
# print(combineColors(app, "#481C0A", "#481C0A"))

# app started: load
# timer fired: pickle.dump