# main file to run animation
# import all files
from cmu_112_graphics_openCV import *
from classes import *
from home import *
from cafe import *
from makeDrink import *
# from latteArt import *
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

    app.mode = 'makeDrinkMode'
    print(app.mode)
    app.cameraOpen = False
    app.timerDelay = 100000

    # cafe grid layout
    app.rows, app.cols, app.cellSize, app.margin = cafeDimensions()
    app.margin = 20
    app.emptyColor = "pink"
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]
   
    # characters
    baristaImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/barista.jpg"),1/20))
    app.barista = Character("barista", 370, 120, baristaImg)
    waiterImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/waiter.jpg"),1/20))
    app.waiter = Character("waiter", 370, 370, waiterImg)
    app.activeChar = app.barista

    # customers
    girl1Img = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/girl1.png"),1/20))
    app.custImgs = [girl1Img]
    app.customers = []
    app.currCustomer = None
    app.isOrdering = False

    # orders
    app.cup = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/topviewcup.png"), 0.9))
    app.orders = ['Latte', 'Macchiato', 'Cappucino', 'Cortado']
    app.espresso = Base("espresso", "brown", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/coffebeans.png"),1/7)))
    app.dairy = Base("dairy", "snow2", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/dairymilk.png"),1/7)))
    app.oat = Base("oat", "blanchedalmond", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/oatmilk.png"),1/7)))
    app.soy = Base("soy", "blancedalmond", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/soymilk.png"),1/7)))
    app.almond = Base("almond", "blancedalmond", ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/almondmilk.png"),1/7)))
    app.bases = ["espresso", "dairy", "oat", "soy", "almond"]
    app.currBase = None
    app.foam = ['foam']
    app.arts = ['heart', 'star', 'flower']
    app.currOrder = set()
    app.drinkMade = set()

    # app.flavors

    # misc items
    cofMacImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cofmac.png"),1/20))
    app.cofMac = Furniture("cofMac", 300, 300, cofMacImg)

    app.rightArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/rightarrow.png"), 1/2))
    # app.furniture = [cofMac]

    app.clockTimer = []
    app.progressbar = []

    # openCV
    app.vid = None

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

# app started: load
# timer fired: pickle.dump