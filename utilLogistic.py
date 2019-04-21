import threading

from utilInformation import *
from utilControl import *
from utilDriver import *
from utilContext import *

PL_mainScreenLogi = [((1572, 75), (198, 203, 57)), ((1594, 52), (148, 158, 41))]
PL_mainScreenLogiDark = [((1594, 52), (74, 77, 16)), ((1575, 73), (99, 101, 24))]
logisticClick = ((1026, 681), (56.0, 30.0), 0)

def toggleLogi():
    #will need to be able to run this while runs are going
    cd.LOGISTIC_RUNNING = not cd.LOGISTIC_RUNNING

def initLogi():
    logi = threading.Thread(None, loopLogi, 'logi')
    logi.start()

#utilManagement will increment a wait value, this will make sure to decrement it (separate looping conditions)
def loopLogi():
    while not cd.COMMIT_SUDOKU:
        wait(0.5, 0.2)
        if cd.LOGISTIC_RUNNING and not cd.MAP_RUNNING:
            if checkPixels(PL_mainScreenLogi) or checkPixels(PL_mainScreenLogiDark):
                rClick(*logisticClick)
        while cd.logiWait > 0:
            if checkPixels(PL_mainScreenLogi) or checkPixels(PL_mainScreenLogiDark):
                cd.logiWait -= 1
                while checkPixels(PL_mainScreenLogi) or checkPixels(PL_mainScreenLogiDark):
                    rClick(*logisticClick)
                    wait(0.5, 0.2)
            wait(0.5, 0.2)