import os, time, select, sys, time, queue, subprocess
import cursor
import inputSystem, visuals, character

def handleQuiting(key):
    if ord(key) == inputSystem.Keycode.Esc: 
        sys.exit()

def playerControls():
    if (inputSystem.hasPressedKey()):
        key = inputSystem.getInputs()
        handleQuiting(key)
        character.updatePosition(key)

def handleAI():
    pass

def update():
    while(True):
        playerControls()
        handleAI()
        visuals.render()

def init():
    cursor.hide()
    character.createPlayer(1, 1, '@', visuals.TextColours.Blue())


def main():
    init()
    update()

if __name__ == "__main__":
    main()
