import os
from src.inputSystem import Keycode

player = None

class Character:
    def __init__(self, X, Y, char, colour):
        self.posX = X
        self.posY = Y
        self.char = char
        self.color = colour

    @staticmethod
    def createPlayer(x, y, char, colour):
        global player
        player = Character(x, y, char, colour)
        return player

    @staticmethod
    def getPlayer():
        global player
        return player

    @staticmethod
    def getPlayerColour():
        global player
        return player.color

    @staticmethod
    def updatePosition(inputChar):
        global player
        world_size = os.get_terminal_size() 

        if ord(inputChar) == Keycode.Up: # Move up
            player.posX -= 1
            if (player.posX < 1):
                player.posX = 1
        if ord(inputChar) == Keycode.Down: # Move down
            player.posX += 1
            if (player.posX > world_size.lines):
                player.posX = world_size.lines
        if ord(inputChar) == Keycode.Left: # Move left
            player.posY -= 1
            if (player.posY < 1):
                player.posY = 1
        if ord(inputChar) == Keycode.Right: # Move right
            player.posY += 1
            if (player.posY > world_size.columns):
                player.posY = world_size.columns