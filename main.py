# main file to run animation
# import all files
from cmu_112_graphics_openCV import *
from classes import *
from home import *
from cafe import *
from makeDrink import *
from latteArt import *
import tkinter as tk
import pickle

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
    app.timerDelay = 150

    # cafe grid layout
    app.rows, app.cols, app.cellSize, app.margin = cafeDimensions()
    app.margin = 20
    app.emptyColor = "pink"
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]
   
    # characters
    baristaImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/barista.jpg"),1/20))
    app.barista = Character("barista", 70, 70, baristaImg)
    waiterImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/waiter.jpg"),1/20))
    app.waiter = Character("waiter", 120, 120, waiterImg)
    app.activeChar = app.barista

    # misc items
    cofMacImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/cofmac.png"),1/20))
    app.cofMac = Furniture("cofMac", 300, 300, cofMacImg)

    app.rightArrowImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/rightarrow.png"), 1/2))
    # app.furniture = [cofMac]

    app.clockTimer = []
    app.progressbar = []


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
  

runApp(width = 540, height = 540)

# app started: load
# timer fired: pickle.dump