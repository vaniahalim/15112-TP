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
    def __init__(self, name, x, y, img, drink, base, art, order, pastry=None):
        self.name = name
        self.x = x
        self.y = y
        self.drink = drink
        self.base = base
        self.art = art
        self.img = img
        self.order = order
        self.pastry = pastry

# pathfinding: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
class Node():
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.startToCurr = 0
        self.currToEnd = 0
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position

# playing music
# SOURCE: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWithPygame
import pygame

class Sound(object):
    def __init__(self, path):
        self.path = path
        self.loops = 1
        pygame.mixer.music.load(path)

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=1):
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        pygame.mixer.music.stop()

# helper: check character distance to object
def distance(x0, y0, x1, y1):
    return (((x0-x1)**2 + (y0-y1)**2)**0.5)

# helper: get cell from coordinates
def getRow(app, y):
    row = int((y - app.margin) / app.cellSize)
    return row

def getCol(app, x):
    col = int((x - app.margin) / app.cellSize)
    return col
