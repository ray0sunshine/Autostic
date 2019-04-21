import win32ui as win
import win32gui as wgui
import threading

class ContextData:
    lock = None
    emuWindow = None
    context = None
    winX = None
    winY = None
    winX2 = None
    winY2 = None

    firstOrder = True
    runsDone = 0
    runsLimit = 10
    burnFodder = 0
    burnFodderLimit = 0
    repairSkip = 0
    repairSkipLimit = 0

    logiCountdown = [None, None, None, None]
    logiWait = 0

    COMMIT_SUDOKU = False
    LOGISTIC_RUNNING = True
    MAP_RUNNING = False
    DEBUG_RUNNING = False
    RUNTIME = 0

    username = ''
    password = ''
    clickDps1 = (((0, 0), (0, 0), 0), 0.8, 0.5, False)
    clickDps2 = (((0, 0), (0, 0), 0), 0.8, 0.5, False)
    clickDps1_02 = (((0, 0), (0, 0), 0), 0.8, 0.5, False)
    clickDps2_02 = (((0, 0), (0, 0), 0), 0.8, 0.5, False)
    retreats_02 = []

    globalx = 0
    globaly = 0

#use this data obj across files
cd = ContextData()

#window context is cached at the start
def initContext(emu):
    if cd.lock == None:
        cd.lock = threading.Lock()
    cd.emuWindow = win.FindWindow(None, emu)
    cd.context = cd.emuWindow.GetWindowDC()
    cd.winX, cd.winY, cd.winX2, cd.winY2 = wgui.GetWindowRect(wgui.FindWindow(None, emu))
    cd.context.DeleteDC()

def toggleFirstOrder():
    cd.firstOrder = not cd.firstOrder

def resetProgress():
    cd.runsDone = 0
    cd.burnFodder = 0
    cd.repairSkip = 0

def incrementRun():
    cd.runsLimit += 1

def decrementRun():
    cd.runsLimit = max(0, cd.runsLimit - 1)

def incrementBurn():
    cd.burnFodderLimit += 1

def decrementBurn():
    cd.burnFodderLimit = max(0, cd.burnFodderLimit - 1)

def incrementRepair():
    cd.repairSkipLimit += 1

def decrementRepair():
    cd.repairSkipLimit = max(0, cd.repairSkipLimit - 1)

def incrementLogiWait():
    cd.logiWait += 1

def decrementLogiWait():
    cd.logiWait = max(0, cd.logiWait - 1)