import os, msvcrt, sys
from enum import IntEnum

class Keycode(IntEnum):
    Esc = 27
    Up = 119
    Down = 115
    Left = 97
    Right = 100

class Input(object):
    @staticmethod
    def __get_char():
        return msvcrt.getch().decode('utf-8')

    @staticmethod
    def get_arrow_hit():
        c = msvcrt.getch()
        vals = [72, 77, 80, 75]
        return vals.index(ord(c.decode('utf-8')))

    @staticmethod
    def has_pressed_key():
        return msvcrt.kbhit()

    @staticmethod
    def clear_pressed_key():
        return msvcrt.kbhit()

    @staticmethod
    def get_inputs():
        input = None

        if Input.has_pressed_key():
            input = Input.__get_char()

        return input