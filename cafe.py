# SCREEN: cafeMode

# SOURCES:
# coffee machine image: 


# import modules
from cmu_112_graphics_openCV import *
import tkinter
import classes

'''''''''''''''''''''''''''''''''
MODEL
'''''''''''''''''''''''''''''''''
# helper: structure of cafe
def cafeDimensions():
    rows = 10
    cols = 10
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
    # draw coffee machine
    canvas.create_image(app.cofMac.x, app.cofMac.y, image=app.cofMac.img)
    

# draw grid of cafe
def drawLayout(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x1,y1,x2,y2) = getCellBounds(app, row, col)
            canvas.create_rectangle(x1, y1, x2, y2, fill= app.board[row][col], width=4, outline='white')

# helper: get coordinates of each cell in grid
def getCellBounds(app, row, col): 
    x1 = app.margin + (col * app.cellSize)
    y1 = app.margin + (row * app.cellSize)
    x2 = app.margin + ((col + 1) * app.cellSize)
    y2 = app.margin + ((row + 1) * app.cellSize)

    return [x1,y1,x2,y2]
    
'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def cafeMode_timerFired(app):
    # CITATION(barista): https://www.vectorstock.com/royalty-free-vector/bearded-barista-man-icon-isometric-style-vector-30590888
    print(distance(app.activeChar.x, app.activeChar.y, app.cofMac.x, app.cofMac.y))


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
    drow *=10
    dcol *=10
    char = app.activeChar
    char.x += drow
    char.y += dcol
    
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

# helper fn: check character distance to object
def distance(x0, y0, x1, y1):
    return (((x0-x1)**2 + (y0-y1)**2)**0.5)


