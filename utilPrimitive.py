import pytesseract as ts
import winsound
import ctypes
import numpy
import time
import math
import sys
import re

from desktopmagic.screengrab_win32 import getRectAsImage
from utilContext import *

MOUSEEVENTF_MOVE = 0x0001       # mouse move
MOUSEEVENTF_LEFTDOWN = 0x0002   # left button down
MOUSEEVENTF_LEFTUP = 0x0004     # left button up
MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
MOUSEEVENTF_MIDDLEUP = 0x0040   # middle button up
COMMIT_SUDOKU = False

#return a weighted point between 2 points
def midPoint(p1, p2, ratio = 0.5):
    inverse = 1 - ratio
    return int(p1[0] * inverse + p2[0] * ratio), int(p1[1] * inverse + p2[1] * ratio)

#returns the distance between 2 points rounded down
def intDist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return int(math.sqrt(dx * dx + dy * dy))

#given a central value and deviation range, return the bounded random value
def normalRange(mean, dev):
    if dev == 0:
        return mean
    return numpy.clip(numpy.random.normal(mean, dev/3.5), mean - dev, mean + dev)

#returns a normal distributed random point near x,y with 3.5 deviantion at devX,devY
#if r the radius is defined, the distance of return to center will be bound be r
def randPoint(p, dev, r = 0):
    rx = normalRange(p[0], dev[0])
    ry = normalRange(p[1], dev[1])
    if r > 0:
        while (rx - p[0])**2 + (ry - p[1])**2 >= r**2:
            rx = normalRange(p[0], dev[0])
            ry = normalRange(p[1], dev[1])
    return rx, ry

#return position based on 4 points and t
def cubicBezier(p1, p2, p3, p4, t):
    t = numpy.clip(t, 0, 1)
    ivt = 1 - t
    xa = [p1[0], 3 * p2[0], 3 * p3[0], p4[0]]
    ya = [p1[1], 3 * p2[1], 3 * p3[1], p4[1]]
    tm = t
    ivtm = ivt
    for i in range(1, 4):
        xa[i] *= tm
        ya[i] *= tm
        tm *= t
    for i in range(2, -1, -1):
        xa[i] *= ivtm
        ya[i] *= ivtm
        ivtm *= ivt
    return sum(xa), sum(ya)

# can only be used to initialize the mouse position
def mouseTo(p):
    ctypes.windll.user32.SetCursorPos(int(p[0] + cd.winX + cd.globalx), int(p[1] + cd.winY + cd.globaly))

# pass in local coords as point tuple
def click(p):
    mouseTo(p)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# use this to actually move the mouse, need to shift a bit to actually lock in position
def mouseMove(p):
    mouseTo(p)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, 1, 1, 0, 0)

# mouse shift by 1 pixel
def mouseShift(x, y):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, x, y, 0, 0)

# can be used in conjunction with mouseTo
def mouseDown():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

# release
def mouseUp():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# mouse middle click
def middleClick():
    p = midPoint((cd.winX, cd.winY), (cd.winX2, cd.winY2))
    p = randPoint((888, 666), (100, 100), 100)
    mouseTo(p)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN | MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)

#if thread much dishonors famiry, much commit sudoku
def bushido():
    if cd.COMMIT_SUDOKU:
        print('Great Dishonor!')
        sys.exit()

#delay, will kill thread if dishonor detected
def wait(t, dev = -1):
    bushido()
    ts = t
    if dev == -1:
        ts = max(normalRange(0.1666, 0.1), normalRange(t + 0.2, 0.2))
    elif dev != 0:
        ts = max(0.001, normalRange(t, dev))
    #print(round(ts,3))
    time.sleep(ts)
    bushido()

#kill application
def kill():
    print('Allahu Ackbar!')
    cd.COMMIT_SUDOKU = True
    cd.LOGISTIC_RUNNING = False
    sys.exit()

#alert
def alert():
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

#screenshot and convert to string (Doesn't really work on a non-mainscreen)
def getScreenText(area):
    ret = ts.image_to_string(getRectAsImage(area))
    return ret.strip()

#determines if the string matches a regex for time and returns result in seconds
def getTimer(t):
    if re.match('\d{2}:\d{2}:\d{2}', t):
        return sum(s*d for s,d in zip([3600,60,1], map(int, t.split(':'))))
    return None

#x: 855
#y: 141,254,367,480
#dim: 128,26