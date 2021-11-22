# SCREEN: cafeMode

# SOURCES:
# barista image: https://www.vectorstock.com/royalty-free-vector/bearded-barista-man-icon-isometric-style-vector-30590888
# waiter image: https://www.iconfinder.com/icons/6655714/barista_cartoon_girl_isometric_love_party_woman_icon
# coffee machine image: https://www.vecteezy.com/vector-art/1983572-isometric-coffee-machine-illustrated-on-white-background
# counter image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fcoffee-house-isometric-illustration-coffeeshop-counter-tables-with-chairs-isolated-clipart_10912455.htm&psig=AOvVaw27CZ0GuBOpJH4o8THG1Cgs&ust=1637440249975000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiCg7mipfQCFQAAAAAdAAAAABAP
# sun image: https://www.flaticon.com/packs/nature-92
# moon image: https://www.flaticon.com/premium-icon/moon_1888300?related_id=1888300&origin=pack
# pathfinding: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

# import modules
from cmu_112_graphics_openCV import *
from classes import *
import random
import time

'''''''''''''''''''''''''''''''''
MODEL
'''''''''''''''''''''''''''''''''
# helper: structure of cafe
def cafeDimensions():
    rows = 10
    cols = 10
    cellSize = 50
    margin = 70
    return (rows, cols, cellSize, margin)


'''''''''''''''''''''''''''''''''
VIEW
'''''''''''''''''''''''''''''''''
# SOURCE: my HW6 tetris

# draw canvas
def cafeMode_redrawAll(app, canvas):
    # draw cafe grid
    canvas.create_rectangle(0, 0, app.width, app.height, fill="lightblue", width=1)
    drawLayout(app, canvas)
    canvas.create_rectangle(70, 170, 320, 520, outline = "pale green", width=1)
    # draw score progress bar 
    canvas.create_rectangle(app.width/2 - 100, 590, app.width/2 + 100, 620, fill="grey", width=0.5)
    canvas.create_text(app.width/2, 605, text="Progress...")
    if not app.win and not app.timeOver:
        canvas.create_rectangle(app.width/2 - 100, 590, app.width/2-100+(app.score/app.winScore)*200, 620, fill="pink")
    # draw timer
    canvas.create_image(605, app.height/2, image=app.timerImg)
    if not app.timeOver:
        canvas.create_line(590,170+(app.time),620,170+(app.time), fill="lightblue", width=2)
    canvas.create_image(605, 95, image=app.sunImg)
    canvas.create_image(605, 545, image=app.moonImg)

    # draw barista
    canvas.create_image(app.barista.x, app.barista.y, image=app.barista.img)
    # draw waiter
    canvas.create_image(app.waiter.x, app.waiter.y, image=app.waiter.img)
    # draw customer
    if app.currCustomer != None:
        canvas.create_image(app.currCustomer.x, app.currCustomer.y, image=app.currCustomer.img)
    # draw coffee machine
    canvas.create_image(app.cofMac.x, app.cofMac.y, image=app.cofMac.img)
    # draw tables
    for i in range(random.randint(1,5)):
        canvas.create_image(app.table.x, app.table.y, image=app.table.img)
    if app.isOrdering:
        canvas.create_text(app.width/2, 35, text=app.currCustomer.order)

    # draw path
    if app.isServing:
        for p in app.path:
            canvas.create_oval(p[0]-5,p[1]-5,p[0]+5,p[1]+5)

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

# helper: get cell from coordinates
def getRow(app, y):
    row = int((y - app.margin) / app.cellSize)
    return row

def getCol(app, x):
    col = int((x - app.margin) / app.cellSize)
    return col

'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def cafeMode_timerFired(app):
    # if app.time == 400: 
    #     app.timeOver
    #     app.mode = "endMode"
    #     app.day += 1
    app.time += 0.1
    app.board = [([app.emptyColor] * app.cols) for row in range(app.rows)]
    app.boardGrid[getRow(app, app.cofMac.y)][getCol(app, app.cofMac.x)] == 1
    app.board[getRow(app, app.barista.y)][getCol(app, app.barista.x)] = "blue"
    app.board[getRow(app, app.waiter.y)][getCol(app, app.waiter.x)] = "orchid"
    if app.isEntering:
        app.currCustomer.x += 5
        if app.currCustomer.x == app.barista.x - 50:
            app.isEntering = False
            app.isOrdering = True
    if app.isOrdering:
        app.counter += app.timerDelay
        if (app.counter % 300 == 0):
            app.isOrdering = False
            app.isWaiting = True
    if app.isServing:
        app.barista.x, app.barista.y == 395, 145
        targetPos = (app.currCustomer.x, app.currCustomer.y)
        app.path = pathfinding(app, (395,395), targetPos)
        print(app.path)
        if app.waiter.x == app.currCustomer.x and app.waiter.y == app.currCustomer.y:
            app.mode = "scoreMode"
        
# using arrow keys
def cafeMode_keyPressed(app, event):
    # accept customer order
    if event.key == "Space":
        app.isOrdering = False
        app.isEntering = True
        custImg = app.custImgs[random.randint(0, len(app.custImgs)-1)]
        drink = app.drinks[random.randint(0, len(app.drinks)-1)]
        base = app.bases[random.randint(1, len(app.bases)-1)]
        art = app.arts[random.randint(0, len(app.arts)-1)]
        order = f"{drink} with {base} milk, {art}"
        app.currCustomer = Customer("1", 0, 145, custImg, drink, base, art, order)
        app.customers.append(app.currCustomer)
        print(app.currCustomer.order)
        print(app.currCustomer.art)
        
   
    # toggle beetween characters
    if event.key == "b":
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
            app.currCustomer.x = 95+50*random.randint(0, 4)
            app.currCustomer.y = 95+50*random.randint(2, 8)

    
# helper fn: move characters
def moveChar(app, drow, dcol):
    drow *= 50
    dcol *= 50
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
    if char.x >= 70 and char.x <= 570 and char.y>= 70 and char.y<=570:
        return True
    return False

# helper: pathfinding algorithm
def pathfinding(app, start, end):
    # initialization
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        print(current_node.position)
        current_index = 0
        for index, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        # indicate current index is visited
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        # move up, down, left, right
        for new_position in [(0, -50), (0, 50), (-50, 0), (50, 0)]: 
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > 570 or node_position[0] < 70 or node_position[1] > 570 or node_position[1] < 70:
                print("out of bounds")
                continue

            # Make sure walkable terrain
            if app.boardGrid[getRow(app, node_position[0])][getCol(app, node_position[1])] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.startToCurr = current_node.startToCurr + 1
            child.currToEnd = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.cost = child.startToCurr + child.currToEnd

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.startToCurr > open_node.startToCurr:
                    continue

            # Add the child to the open list
            open_list.append(child)



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

