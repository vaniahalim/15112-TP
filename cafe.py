# SCREEN: cafeMode

# SOURCES:
# barista image: https://www.vectorstock.com/royalty-free-vector/bearded-barista-man-icon-isometric-style-vector-30590888
# waiter image: https://www.iconfinder.com/icons/6655714/barista_cartoon_girl_isometric_love_party_woman_icon
# coffee machine image: https://www.vecteezy.com/vector-art/1983572-isometric-coffee-machine-illustrated-on-white-background
# counter image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fcoffee-house-isometric-illustration-coffeeshop-counter-tables-with-chairs-isolated-clipart_10912455.htm&psig=AOvVaw27CZ0GuBOpJH4o8THG1Cgs&ust=1637440249975000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiCg7mipfQCFQAAAAAdAAAAABAP
# table image: https://www.iconfinder.com/icons/6656008/cartoon_folding_hand_isometric_retro_round_table_icon
# sun image: https://www.flaticon.com/packs/nature-92
# moon image: https://www.flaticon.com/premium-icon/moon_1888300?related_id=1888300&origin=pack
# timer image: https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.xmple.com%2Fwallpaper%2Forange-blue-gradient-linear-1920x1080-c2-0000cd-ff8c00-a-45-f-14.svg&imgrefurl=https%3A%2F%2Fwww.xmple.com%2Fwallpaper%2Forange-blue-gradient-linear--c2-0000cd-ff8c00-a-45-f-14-image%2F&tbnid=Bn41Fc6ZA9X_JM&vet=12ahUKEwjag47pv630AhWLBc0KHW1cAkoQMygOegUIARDyAQ..i&docid=CCYxh7MBUtbZdM&w=1920&h=1080&itg=1&q=orange%20blue%20gradient&ved=2ahUKEwjag47pv630AhWLBc0KHW1cAkoQMygOegUIARDyAQ
# people images: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fcreative-pack-isometric-people-flat-icons-providing-awesome-features-human-avatars-performing-various-activities-image125598730&psig=AOvVaw2gdVQ-_yHhfKPwtFq5cX0K&ust=1637723158290000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJjx9KvArfQCFQAAAAAdAAAAABAD
# help image: https://www.flaticon.com/premium-icon/help_2550424?term=help%20button&page=1&position=80&page=1&position=80&related_id=2550424&origin=search
# menu image: https://www.flaticon.com/premium-icon/help_2550424?term=help%20button&page=1&position=80&page=1&position=80&related_id=2550424&origin=search
# plant image: https://www.flaticon.com/free-icon/plant_628283#
# floor image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwallpaperaccess.com%2Flight-wood&psig=AOvVaw09MKrvQMjKpKJVNBXLsf9f&ust=1638128491372000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOCc26qmufQCFQAAAAAdAAAAABAD

# pathfinding: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

# import modules
from cmu_112_graphics_openCV import *
from classes import *
import random

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
    canvas.create_rectangle(0, 0, app.width, app.height, fill="#FFE9DF", width=1)
    drawLayout(app, canvas)
    canvas.create_image(app.width/2, app.height/2, image=app.floorImg)
    # draw instructions 
    canvas.create_image(605, 35, image=app.helpImg)
    # draw score progress bar 
    canvas.create_rectangle(app.width/2 - 100, 590, app.width/2 + 100, 620, fill="lightgrey", width=0.5)
    if not app.win and not app.timeOver:
        canvas.create_rectangle(app.width/2 - 100, 590, app.width/2-100+(app.score/app.winScore)*200, 620, fill="pink")
        canvas.create_text(app.width/2, 605, text="Progress...")
    if app.win:
        canvas.create_rectangle(app.width/2 - 100, 590, app.width/2 + 100, 620, fill="pink", width=0.5)
        canvas.create_text(app.width/2, 605, text="Complete!")
    # draw timer
    canvas.create_image(605, app.height/2, image=app.timerImg)
    if not app.timeOver:
        canvas.create_line(590,120+(app.time/app.gameTime)*400,620,120+(app.time/app.gameTime)*400, fill="lightblue", width=2)
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
    if app.closeCofMac:
        canvas.create_text(app.width/2, 35, text="Press enter to make drinks!")
    # draw tables
    for table in app.tables:
        canvas.create_image(table.x, table.y, image=table.img)
    canvas.create_image(345, 145, image=app.counterImg)
    # draw plants
    for x in range(95, 555, 50):
        canvas.create_image(x, 95, image=app.plantImg)
        canvas.create_image(x, 545, image=app.plantImg)
     # draw menu
    canvas.create_image(app.menu.x, app.menu.y, image=app.menu.img)
    
    # draw order text
    if app.isOrdering:
        canvas.create_text(app.width/2, 35, text=app.currCustomer.order)
    if app.isStarting:
        canvas.create_text(app.width/2, 35, text="Press space to accept orders!")

    # draw path
    if app.isServing:
        for p in app.path:
            canvas.create_oval(p[0]-5,p[1]-5,p[0]+5,p[1]+5, fill="green")

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


'''''''''''''''''''''''''''''''''
CONTROLLER
'''''''''''''''''''''''''''''''''
def cafeMode_timerFired(app):
    # set up board
    for row in range(10):
        for col in range(10):
            if row == getRow(app,app.activeChar.y) and col == getCol(app,app.activeChar.x):
                app.board[row][col] = "blue"
            else:
                app.board[row][col] = app.emptyColor

    # end of day
    if app.time >= app.gameTime: 
        app.timeOver
        app.mode = "endMode"

    # modify difficulty of game:
    if app.time > 0 and app.time % 1000 == 0:
        checkDifficulty(app)

        # difficulty level changes if player becomes better/worse 
        # changes number of drinks, score threshold, time order is shown, number of tables (obstacles)
        if app.difficulty[-1] == "easy":
            app.drinksShown = max(app.drinksShown-1, 2)
            app.scoreThresh = min(app.scoreThresh+0.1, 0.6)
            app.orderTime = min(app.orderTime+50, 600)
            app.tableNo = max(app.tableNo-1, 2)
        if app.difficulty[-1] == "normal":
            app.drinksShown = 4
            app.scoreThresh = 0.4
            app.orderTime = 400
            app.tableNo = 5
        if app.difficulty[-1] == "hard":
            app.drinksShown = min(app.drinksShown+1, 7)
            app.scoreThresh = max(app.scoreThresh-0.1, 0.2)
            app.orderTime = max(app.orderTime-50, 300)
            app.tableNo = min(app.tableNo+1, 7)

    # count down timer increases
    app.time += 1

    # show instruction to go to makeDrinkMode
    if distance(app.activeChar.x, app.activeChar.y, app.cofMac.x, app.cofMac.y) <= 50:
        app.closeCofMac = True
    elif distance(app.activeChar.x, app.activeChar.y, app.cofMac.x, app.cofMac.y) > 50:
        app.closeCofMac = False

    # customer enters
    if app.isEntering:
        app.currCustomer.x += 10
        if app.currCustomer.x >= 295:
            app.isEntering = False
            app.isOrdering = True
    # show order 
    if app.isOrdering:
        app.counter += app.timerDelay
        if (app.counter == app.orderTime):
            app.isOrdering = False
            app.isWaiting = True
    # barista serving drink to customer
    if app.isServing:
        app.barista.x, app.barista.y = 395, 145
        startPos = (app.waiter.x, app.waiter.y)
        targetPos = (app.currCustomer.x, app.currCustomer.y)
        app.path = pathfinding(app, startPos, targetPos)
        if (app.waiter.x == app.currCustomer.x) and (app.waiter.y == app.currCustomer.y):
            app.mode = "scoreMode"

# helper: check how good player is to modify game difficulty
def checkDifficulty(app):
    if app.score/app.winScore < app.time/app.gameTime:
        app.difficulty.append("easy")
    if app.score/app.winScore == app.time/app.gameTime:
        app.difficulty.append("normal")
    if app.score/app.winScore > app.time/app.gameTime:
        app.difficulty.append("hard")      

# using arrow keys
def cafeMode_keyPressed(app, event):
    # accept customer order
    if event.key == "Space":
        app.isStarting = False
        app.isOrdering = False
        app.isEntering = True
        custImg = app.custImgs[random.randint(0, len(app.custImgs)-1)]
        drink = app.drinks[random.randint(0, app.drinksShown-1)]
        base = app.bases[random.randint(1, len(app.bases)-1)]
        art = app.arts[random.randint(0, len(app.arts)-1)]
        order = f"{drink} with {base} milk, {art}"
        app.currCustomer = Customer("1", 0, 145, custImg, drink, base, art, order)
        print(app.currCustomer.order)
        
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
        if app.currCustomer != None:
            if event.key == "Return" or event.key == "Enter":
                app.mode = "makeDrinkMode"
                app.currCustomer.x, app.currCustomer.y = getRandPos(app)
    
    # check menu
    elif distance(app.activeChar.x, app.activeChar.y, app.menu.x, app.menu.y) <= 50:
        if event.key == "Return" or event.key == "Enter":
            app.mode = "menuMode"

# helper: recursive function to get random available position for customer to stand at
def getRandPos(app):
    randX = 95+50*random.randint(0, 4)
    randY = 95+50*random.randint(2, 8)
    if app.boardGrid[getRow(app, randY)][getCol(app, randX)] == 0:
        return randX, randY
    else:
        return getRandPos(app)
    
# helper: move characters
def moveChar(app, drow, dcol):
    drow *= 50
    dcol *= 50
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
    if char.x >= 70 and char.x <= 570 and char.y>= 120 and char.y<=570 and (app.boardGrid[getRow(app, char.y)][getCol(app, char.x)] == 0):
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

    # iterate until target location is reached
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        # indicate current index is visited
        open_list.pop(current_index)
        closed_list.append(current_node)

        # reached target
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] 

        # Generate children
        children = []
        # move up, down, left, right
        for new_position in [(0, -50), (0, 50), (-50, 0), (50, 0)]: 
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # check legality of move in board
            if (node_position[0] > 495) or (node_position[0] < 95) or (node_position[1] > 495) or (node_position[1] < 195):
                continue
            # if app.boardGrid[getRow(app, node_position[0])][getCol(app, node_position[1])] != 0:
            #     print("0 detected")
            #     continue

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

def cafeMode_mousePressed(app, event):
    x = event.x
    y = event.y

    if distance(x, y, 605, 35) < 30:
        app.mode = "cafeInstructionsMode"




