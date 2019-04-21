import pyautogui as gui
import win32gui as wgui
import threading

from utilContext import *
from utilPrimitive import *

#get color within the window
#getting and releasing the DC each time actually doesn't impact performance, need to make it thread safe though
#DeleteDC crashes fix was to do the lock stuff
#get pix could fail if the window focus is being fought over, but retrying does work
# NOTE:
# The Nox render mode with OpenGL usually works but it fucked up on my laptop (returns white only on game screen...but fine for window ui) and worked again by switching to DirectX
def getColor(x, y):
    cd.lock.acquire()
    SUCCESS = False
    while not SUCCESS:
        try:
            cd.context = cd.emuWindow.GetWindowDC()
            c = cd.context.GetPixel(x + cd.globalx, y + cd.globaly)
            cd.context.DeleteDC()
            SUCCESS = True
        except:
            cd.context.DeleteDC()
            print('get pixel fail')
            wait(0.1)
    cd.lock.release()
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff)

#get mouse position relative to context window
def getMousePos():
    mx, my = gui.position()
    if cd.winX <= mx <= cd.winX2 and cd.winY <= my <= cd.winY2:
        return mx - cd.winX, my - cd.winY
    return None

#get pixel color at mouse, does bound check
def getMouseColor():
    mp = getMousePos()
    if mp != None:
        return getColor(mp[0], mp[1])
    return None

#try to match 2 color tuples, with optional allowance for difference
def matchColor(c1, c2, deviance = 0):
    return max(abs(a - b) for a, b in zip(c1, c2)) <= deviance