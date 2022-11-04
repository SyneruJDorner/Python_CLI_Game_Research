import os, time, select, sys, time, queue, subprocess
import cursor
from src.visuals import visuals
from src.character import Character
from src.inputSystem import Input, Keycode


def handleQuiting(key):
    if ord(key) == Keycode.Esc: 
        sys.exit()


def playerControls():
    if (Input.has_pressed_key()):
        key = Input.get_inputs()
        handleQuiting(key)
        Character.updatePosition(key)


def handleAI():
    pass


def update():
    while(True):
        playerControls()
        handleAI()
        visuals.render()
        #Handle Debugging here!


def init():
    cursor.hide()
    Character.createPlayer(1, 1, '@', visuals.TextColours.Blue())


def main():
    init()
    update()


if __name__ == "__main__":
    main()
