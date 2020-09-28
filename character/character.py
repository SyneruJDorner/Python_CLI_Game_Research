from inputSystem import Keycode

player = None

class Character:
    def __init__(self, X, Y, char, colour):
        self.posX = X
        self.posY = Y
        self.char = char
        self.color = colour

def createPlayer(x, y, char, colour):
    global player
    player = Character(x, y, char, colour)
    return player

def getPlayer():
    global player
    return player

def getPlayerColour():
    global player
    return player.color

def updatePosition(inputChar):
    global player

    if ord(inputChar) == Keycode.Up: # Move up
        player.posX -= 1
    if ord(inputChar) == Keycode.Down: # Move down
        player.posX += 1
    if ord(inputChar) == Keycode.Left: # Move left
        player.posY -= 1
    if ord(inputChar) == Keycode.Right: # Move right
        player.posY += 1