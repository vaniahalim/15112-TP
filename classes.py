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

class Drink(object):
    def __init__(self, name):
        self.name = name
        self.depth = 0
        self.color = ""

class Art(object):
    def __init__(self):
        self.color = ""


# helper fn: check character distance to object
def distance(x0, y0, x1, y1):
    return (((x0-x1)**2 + (y0-y1)**2)**0.5)