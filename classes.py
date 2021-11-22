# character classes for barista and waiter
class Character(object):
    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = img

class Furniture(object):
    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = img

class Base(object):
    def __init__(self, name, color, img):
        self.name = name
        self.color = color
        self.img = img
        self.r = 0

class Art(object):
    def __init__(self):
        self.color = ""

class Customer(object):
    def __init__(self, name, x, y, img, drink, base, art, order):
        self.name = name
        self.x = x
        self.targetx = 0
        self.targety = 0
        self.y = y
        self.drink = drink
        self.base = base
        self.art = art
        self.img = img
        self.order = order

# pathfinding
class Node():
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.startToCurr = 0
        self.currToEnd = 0
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position

# helper fn: check character distance to object
def distance(x0, y0, x1, y1):
    return (((x0-x1)**2 + (y0-y1)**2)**0.5)