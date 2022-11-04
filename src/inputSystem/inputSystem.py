import os, msvcrt, sys
from enum import IntEnum

class Keycode(IntEnum):
    Esc = 27
    Up = 119
    Down = 115
    Left = 97
    Right = 100

class KBHit(object):
    @staticmethod
    def getCharHit():
        return msvcrt.getch().decode('utf-8')

    @staticmethod
    def getArrowHit():
        c = msvcrt.getch()
        vals = [72, 77, 80, 75]
        return vals.index(ord(c.decode('utf-8')))

    @staticmethod
    def hasPressedKey():
        return msvcrt.kbhit()

    @staticmethod
    def clearPressedKey():
        return msvcrt.kbhit()

def hasPressedKey():
    return KBHit.hasPressedKey()

def getInputs():
    inputChar = None

    if hasPressedKey():
        inputChar = KBHit.getCharHit()

    return inputChar