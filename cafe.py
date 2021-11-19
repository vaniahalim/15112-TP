# SCREEN: cafeMode

# SOURCES:
# barista image: https://www.vectorstock.com/royalty-free-vector/bearded-barista-man-icon-isometric-style-vector-30590888
# waiter image: https://www.iconfinder.com/icons/6655714/barista_cartoon_girl_isometric_love_party_woman_icon
# coffee machine image: https://www.vecteezy.com/vector-art/1983572-isometric-coffee-machine-illustrated-on-white-background
# cup image: 

# import modules
from cmu_112_graphics_openCV import *
from classes import *
import random

'''''''''''''''''''''''''''''''''
MODEL
'''''''''''''''''''''''''''''''''
# helper: structure of cafe
def cafeDimensions():
    rows = 12
    cols = 12
    cellSize = 50
    margin = 20
    return (rows, cols, cellSize, margin)

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
# referenced from my HW6: tetris

# draw canvas
def cafeMode_redrawAll(app, canvas):
    # draw cafe
    canvas.create_rectangle(0, 0, app.width, app.height, fill="lightblue", width=1)
    drawLayout(app, canvas)
    # draw barista
    canvas.create_image(app.barista.x, app.barista.y, image=app.barista.img)
    # draw waiter
    canvas.create_image(app.waiter.x, app.waiter.y, image=app.waiter.img)
    # draw customer
    if app.currCustomer != None:
        canvas.create_image(app.currCustomer.x, app.currCustomer.y, image=app.currCustomer.img)
    # draw coffee machine
    canvas.create_image(app.cofMac.x, app.cofMac.y, image=app.cofMac.img)

    if app.isOrdering:
        canvas.create_text(app.currCustomer.x, app.currCustomer.y + 10, text=app.currCustomer.order)

    

# draw grid of cafe
def drawLayout(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x1,y1,x2,y2) = getCellBounds(app, row, col)
            canvas.create_rectangle(x1, y1, x2, y2, fill= app.board[row][col], width=4, outline="white")

# helper: get coordinates of each cell in grid
def getCellBounds(app, row, col): 
    x1 = app.margin + (col * app.cellSize)
    y1 = app.margin + (row * app.cellSize)
    x2 = app.margin + ((col + 1) * app.cellSize)
    y2 = app.margin + ((row + 1) * app.cellSize)

    return [x1,y1,x2,y2]


# 2d to isometric
# SOURCES:
# https://gamedevelopment.tutsplus.com/tutorials/creating-isometric-worlds-primer-for-game-developers-updated--cms-28392
# https://gamedevelopment.tutsplus.com/tutorials/updated-primer-for-creating-isometric-worlds-continued--cms-28503

# def cartIso(app,cartX, cartY):
#     isoX = (cartX - cartY) * app.cellSize/2
#     isoY = (cartX + cartY)/2
#     return isoX, isoY

# def isoCart(isoX, isoY):
#     cartX = (2*isoY + isoX)/2
#     cartY = (2*isoY - isoX)/2
#     return cartX, cartY

#  def cartToIso(self, cartX, cartY, scalingFactor):
#         cartX -= self.offsetX 
#         cartY -= self.offsetY 
#         cartX = cartX / scalingFactor
#         cartY = cartY / scalingFactor 
#         isoX = cartX - cartY
#         isoY = (cartX + cartY) / 2
#         return isoX, isoY

#     def isoToCart(self, isoX, isoY, scalingFactor):
#         cartX = (2 * isoY + isoX) / 2
#         cartY = (2 * isoY - isoX) / 2
#         cartX = cartX / scalingFactor
#         cartY = cartY / scalingFactor
#         cartX += offsetX 
#         cartY += offsetY 
#         return cartX, cartY 

#     def setUpIsometric(self):
#         #self.tileWidthHalf = self.tileWidth//2
#         #self.tileHeightHalf = self.tileHeight//2
#         self.offsetX = -1000
#         self.offsetY = -270


    
'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def cafeMode_timerFired(app):
    # if app.isNewCustomer:
    custImg = app.custImgs[random.randint(0, len(app.custImgs)-1)]
    order = f"{app.orders[random.randint(0, len(app.orders)-1)]} with {app.bases[random.randint(0, len(app.bases)-1)]} milk, {app.arts[random.randint(0, len(app.arts)-1)]}"
    # app.currOrder = [app.orders[ran]]
    app.currCustomer = Customer("1", 0, 120, custImg, order)
    app.customers.append(app.currCustomer)

    # while app.currCustomer.x < app.barista.x - 10:
    app.currCustomer.x += 10
    # if app.currCustomer.x == app.barista.x - 10:
    #     app.isOrdering = True
    #     app.currCustomer.x = app.barista.x - 10
    print(app.currCustomer.x)

# using arrow keys
def cafeMode_keyPressed(app, event):
    # toggle beetween characters
    if event.key == "Space":
        app.activeChar = app.waiter if app.activeChar == app.barista else app.barista
    # using arrow keys to move
    if event.key == "Left":
        moveChar(app, -1, 0)
    elif event.key == "Up":
        moveChar(app, 0, -1)
    elif event.key == "Down":
        moveChar(app, 0, +1)
    elif event.key == "Right":
        moveChar(app, +1, 0)
    
    # switch to makedrink mode
    elif distance(app.activeChar.x, app.activeChar.y, app.cofMac.x, app.cofMac.y) <= 50:
        if event.key == "Return" or event.key == "Enter":
            print("close")
            app.mode = "makeDrinkMode"
    
# helper fn: move characters
def moveChar(app, drow, dcol):
    drow *= 10
    dcol *= 10
    char = app.activeChar
    char.x += drow
    char.y += dcol
    # char.isoX, char.isoY = cartIso(char.x, char.y)
    
    if not moveIsLegal(app):
        char.x -= drow
        char.y -= dcol
    return True

# helper fn: check if move can be made (not out of bounds)
def moveIsLegal(app):
    char = app.activeChar
    if char.x >= 0 and char.x <= app.width and char.y>= 0 and char.y<=app.height:
        return True
    return False




