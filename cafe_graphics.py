# 3D graphics of cafe layout

# import graphics
from opencv.cmu_112_graphics_openCV import *

# class cafeScreen(object):
'''''''''''''''''''''''''''''''''
MODEL
'''''''''''''''''''''''''''''''''
def appStarted(app):
    app.isCafeScreen = True
    app.timerDelay = 150

    # items in cafe
    app.character = "barista"
    app.furniture = []
    app.clockTimer = []
    app.progressbar = []

    # cafe grid layout
    app.rows, app.cols, app.cellSize, app.margin = cafeDimensions()
    app.emptyColor = "pink"
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]

# helper: structure of cafe
def cafeDimensions():
    rows = 10
    cols = 10
    cellSize = 50
    margin = 20
    return (rows, cols, cellSize, margin)

# intialize/get barista coordinates
def barista(app, row, col):
    app.bar_x = getCellBounds(app, row, col)[0] 
    app.bar_y = getCellBounds(app, row, col)[3]

# initialize/get waiter position
def waiter(app, row, col):
    app.waiter_x = getCellBounds(app, row, col)[0] 
    app.waiter_y = getCellBounds(app, row, col)[3] 

'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
# referenced from HW6: tetris

# draw canvas
def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="lightblue", width=1)
    drawLayout(app, canvas)
    drawBarista(app, canvas)

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

# draw barista
def drawBarista(app, canvas):
    canvas.create_oval(app.bar_x, app.bar_y, app.bar_x+10, app.bar_y+10, fill="purple")


    
'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
# using arrow keys
def keyPressed(app, event):
    if event.key == "Up":
        moveChar(app, -1, 0)
    elif event.key == "Left":
        moveChar(app, 0, -1)
    elif event.key == "Right":
        moveChar(app, 0, +1)
    elif event.key == "Down":
        moveChar(app, +1, 0)
    
    # switch character
    elif event.key == "Space":
        if app.character == "barista":
            app.character = "waiter"
        else:
            app.character = "barista"
    
# helper: move characters
def moveChar(app, drow, dcol):
    # move barista
    if app.character == "barista":
        app.bar_x += drow
        app.bar_y +=  dcol
       
        if not moveIsLegal(app):
            app.bar_x -= drow
            app.bar_y -=  dcol
            return False
    # move waiter
    if app.character == "waiter":
        app.waiter_x += drow
        app.waiter_y +=  dcol
        
        if not moveIsLegal(app):
            app.waiter_x -= drow
            app.waiter_y -=  dcol
            return False
    return True

# helper: check if move can be made (not out of bounds, empty)
def moveIsLegal(app):
    is 






# load cafe screen
def loadCafeScreen():
    rows, cols, cellSize, margin = cafeDimensions()
    w = (cols * cellSize) + (2 * margin)
    h = (rows * cellSize) + (2 * margin)
    runApp(width=w, height=h)


loadCafeScreen()
# if __name__ == '__loadCafeScreen__':
#     loadCafeScreen()

# cafe = cafeScreen()
# cafe.loadCafeScreen()
