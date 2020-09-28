import os
import sys
import character

class TextColours(object):
    @staticmethod
    def Black():
        return "\x1b[1;30m"

    @staticmethod
    def Red():
        return "\x1b[1;31m"

    @staticmethod
    def Green():
        return "\x1b[1;32m"

    @staticmethod
    def Yellow():
        return "\x1b[1;33m"

    @staticmethod
    def Blue():
        return "\x1b[1;34m"

    @staticmethod
    def Magenta():
        return "\x1b[1;35m"

    @staticmethod
    def Cyan():
        return "\x1b[1;36m"

    @staticmethod
    def White():
        return "\x1b[1;37m"

    @staticmethod
    def BrightBlack():
        return "\x1b[1;90m"

    @staticmethod
    def BrightRed():
        return "\x1b[1;91m"

    @staticmethod
    def BrightGreen():
        return "\x1b[1;92m"

    @staticmethod
    def BrightYellow():
        return "\x1b[1;93m"

    @staticmethod
    def BrightBlue():
        return "\x1b[1;94m"

    @staticmethod
    def BrightMagenta():
        return "\x1b[1;95m"

    @staticmethod
    def BrightCyan():
        return "\x1b[1;96m"

    @staticmethod
    def BrightWhite():
        return "\x1b[1;97m"

clear = lambda: os.system('cls')

def render():
    if not hasattr(render, "buffer") and not hasattr(render, "lastBuffer"):
        render.buffer = ""
        render.lastBuffer = ""

    render.buffer += queueCharactersRender()

    if (render.lastBuffer == render.buffer):
        render.buffer = ""
        return

    clear()
    sys.stdout.write(render.buffer)
    sys.stdout.flush()
    render.lastBuffer = render.buffer
    render.buffer = ""

def resetColour():
    #means we reset the colour usage is like <HTML></HTML>
    #after calling a colour you must ens the colour
    return "\x1b[1;0m"

def queueCharactersRender():
    playerBuffer = character.getPlayerColour()
    #\x1b7          => The instruction "7" means save the cursor information.
    playerBuffer += "\x1b7" 
    #\x1b[%d;%df    => The instruction "[x;yf" means go to row 10, column 10. Your code replaces the %ds with numbers inputted by the user.
    #%s             => This is replaced by the text from the user. No escape character here, so the text is printed normally.
    playerBuffer += "\x1b[%d;%df%s" % (character.getPlayer().posX, character.getPlayer().posY, character.getPlayer().char)
    #\x1b8          => The instruction "8" means restore the cursor information.
    playerBuffer += "\x1b8"
    playerBuffer += resetColour()
    return playerBuffer
