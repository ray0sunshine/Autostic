import threading
import sys

from collections import deque
from utilControl import *
from utilPrimitive import *
from utilInformation import *

#walk queue (on hold key start queue, release = clear)
#normal swapping (on hold key start queue, release = clear)
#queue reverse swap (save latest swap)
#normal select
#retreat
#skill hotkey
#auto toggle hotkey

class MoveData:
    # queue up the swap that need to happen in order
    actionQueue = deque()

    # position list that is cleared on the key releases
    positionQueue = deque()

    # keep most recently executed swap
    lastSwap = None

md = MoveData()

# do position swaps with a bit of random
def reposition(a, b):
    rHoldDrag(randPoint(*a), randPoint(*b), 24, 0.1, 0.05)

# shift the screen far right, then shift it back exactly 204 pixel
def resetScreen():
    rHoldDrag(randPoint((958, 180), (25, 30), 0), randPoint((1666, 180), (25, 30), 0), 30, 0.2, 0.05)
    wait(0.05, 0)
    holdStart = randPoint((1004, 180), (25, 30), 0)
    holdEnd = randPoint((holdStart[0] - 204, 180), (2, 30), 0)
    rHoldDrag(holdStart, holdEnd, 30, 0.2, 0.05)
    clearPositionQueue(None)

# select grid boxes and changes behavior based on toggled modes
def positionSelected(target, variance, rad):
    data = (target, variance, rad)
    rClick(*data)

def positionSwapped(target, variance, rad):
    data = (target, variance, rad)
    # don't really want the same position to be queued as a swap
    if len(md.positionQueue) > 0 and data == md.positionQueue[-1]:
        return
    # clears the queue completely when 2 postions are reached
    md.positionQueue.append(data)
    if len(md.positionQueue) > 1:
        md.actionQueue.append((md.positionQueue[-2], md.positionQueue[-1]))
        md.positionQueue.clear()

def positionWalked(target, variance, rad):
    data = (target, variance, rad)
    # don't really want the same position to be queued as a swap
    if len(md.positionQueue) > 0 and data == md.positionQueue[-1]:
        return
    # retains the latest position for next added pos to use
    md.positionQueue.append(data)
    if len(md.positionQueue) > 1:
        md.actionQueue.append((md.positionQueue[-2], md.positionQueue[-1]))
        while len(md.positionQueue) > 1:
            md.positionQueue.popleft()

# run in separate thread
def executeQueue():
    while not cd.COMMIT_SUDOKU:
        if len(md.actionQueue) > 0:
            md.lastSwap = md.actionQueue.popleft()
            reposition(*(md.lastSwap))
        wait(0.04, 0)

def executeMoverThread():
    mover = threading.Thread(None, executeQueue, 'mover')
    mover.start()

def autoToggle():
    rClick((1551, 160), (32, 32), 32)

def reverseSwap():
    if md.lastSwap != None:
        md.actionQueue.append((md.lastSwap[1], md.lastSwap[0]))

def withdraw():
    rClick((413, 202), (24, 24), 24)

def withdrawManual():
    oldPos = getMousePos()
    rClick((413, 202), (24, 24), 24)
    if(oldPos):
        mouseTo(oldPos)

def closeApp():
    rClick((1901, 1035), (7.0, 6.0), 0)

def pause():
    oldPos = getMousePos()
    rClick((942, 46), (24.0, 7.5), 0)
    if(oldPos):
        mouseTo(oldPos)

def skill(target, variance, rad):
    rClick(target, variance, rad)

# the queue gets reset everytime the modifiers are let go so it doesn't carry over
def clearPositionQueue(e):
    md.positionQueue.clear()