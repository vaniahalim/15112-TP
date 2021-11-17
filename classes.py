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
    def __init__(self, name, x, y, img, order):
        self.name = name
        self.x = x
        self.y = y
        self.order = order
        self.art = ""
        self.img = img

# helper fn: check character distance to object
def distance(x0, y0, x1, y1):
    return (((x0-x1)**2 + (y0-y1)**2)**0.5)