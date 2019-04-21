import time
import pyperclip

from utilControl import *
from utilInformation import *
from utilPrimitive import *

#Pixel info is of form tuple(pos,color), color being a tuple as well
#Pixel set array is a list of those info tuples which can be checked using getColor
#pixList is a screen state (hashed to several pixel colors at specified positions)
DEVIANCE_THRESHOLD = 10
LOCK_LIMIT = 30
RETRY_LIMIT = 3

#tracking runtime data
class DriverData:
    currentPL = []

dd = DriverData()

#print the current PL on multiple lines
def stringPL():
    return '\n'.join([str(o) for o in dd.currentPL])

#Add mouse color and position as a tuple to the current stack
def addReferencePixel():
    pos = getMousePos()
    col = getMouseColor()
    if pos != None and col != None:
        dd.currentPL.append((pos, col))
        print('add:\n' + stringPL())

def removeLastReferencePixel():
    if len(dd.currentPL) > 0:
        dd.currentPL.pop()
        print('del:\n' + stringPL())

def clearReferencePixel():
    dd.currentPL.clear()
    print('clear:\n' + stringPL())

#copy all the existing PL points to the clip
def copyPLToClipBoard():
    pyperclip.copy(str(dd.currentPL))
    print('copy:', pyperclip.paste())
    dd.currentPL.clear()

#function to update existing PL
def updatePLToClipBoard(pl):
    pl_out = [(e[0], getColor(e[0][0], e[0][1])) for e in pl]
    pyperclip.copy(str(pl_out))
    print('update:', pyperclip.paste())

#based on the last 2 points recieved, use it as the diameter of a circular click area
#will auto pop the 2 points
def getCircularClick():
    if len(dd.currentPL) >= 2:
        p1 = (dd.currentPL.pop())[0]
        p2 = (dd.currentPL.pop())[0]
        center = midPoint(p1, p2)
        r = intDist(p1, p2) // 2
        #clickObj = ((center, (r, r), r), 0.5, 0.3, False)
        clickObj = (center, (r, r), r)
        pyperclip.copy(str(clickObj))
        print('circle:', pyperclip.paste())

#based on the last 2 points recieved, use them as the TL and BR corner (just gets the limit x y values)
def getRectClick():
    if len(dd.currentPL) >= 2:
        p2 = (dd.currentPL.pop())[0]
        p1 = (dd.currentPL.pop())[0]
        center = midPoint(p1, p2)
        d = (abs(p1[0] - p2[0]) / 2, abs(p1[1] - p2[1]) / 2)
        #clickObj = ((center, d, 0), 0.5, 0.3, False)
        clickObj = (center, d, 0)
        pyperclip.copy(str(clickObj))
        print('rect:', pyperclip.paste())

#based on the last 2 points recieved, use them as the p1 and p4 of the drag
def getDrag():
    if len(dd.currentPL) >= 2:
        p1 = (dd.currentPL.pop())[0]
        p2 = (dd.currentPL.pop())[0]
        clickObj = ((p1, p2, 30, 0.4), 0.1, 0.1, True)
        pyperclip.copy(str(clickObj))
        print('drag:', pyperclip.paste())

#checks if all colors match within the allowed deviation to the current color at the listed coordinates
def checkPixels(pixList):
    return all([matchColor(pix[1], getColor(*(pix[0])), DEVIANCE_THRESHOLD) for pix in pixList])

def diffPixels(pixList, prefix):
    ret = []
    for pix in pixList:
        if not matchColor(pix[1], getColor(*(pix[0])), DEVIANCE_THRESHOLD):
            ret.append(str(pix) + ' vs ' + str(getColor(*(pix[0]))))
    print(prefix + '\n'.join(ret))

#targetPL: list of (pos,color) where pos is (x,y) and color is (r,g,b)
#clickInfo: tuple (pos, dev, r) where pos is (x,y) dev is (w,h), (p1, p4, r, time) as a drag
#conditionWait: seconds to wait for targetPL after initial click
#retryDelay: seconds to wait once in retry cycle
#whilePL: if defined, will check that the action is excuted on a determined PL
def actionUntil(targetPL, clickInfo, conditionWait = 1, retryDelay = 1, whilePL = None, drag = False):
    if checkPixels(targetPL):
        return
    lockTimer = time.clock() + LOCK_LIMIT
    retries = 0
    if drag:
        rDrag(*clickInfo)
        wait(conditionWait, 0.2)
        while not checkPixels(targetPL):
            wait(0.04)
            if time.clock() > lockTimer:
                lockTimer += LOCK_LIMIT
                diffPixels(targetPL, 'target miss:\n')
                alert()
            else:
                rDrag(*clickInfo)
                wait(retryDelay, 0.2)
                retries += 1
                if retries > RETRY_LIMIT:
                    wait(10, 0)
    else:
        if whilePL != None:
            while not checkPixels(whilePL):
                wait(0.04)
                if time.clock() > lockTimer:
                    lockTimer += LOCK_LIMIT
                    diffPixels(whilePL, 'base miss:\n')
                    alert()
                else:
                    wait(1)
            rClick(*clickInfo)
            wait(conditionWait, 0.2)
            if not checkPixels(targetPL):
                # Do initial wait before actually retrying, condition wait is only how long it should usually take
                wait(retryDelay, 0.2)
                while not checkPixels(targetPL):
                    wait(0.04)
                    if time.clock() > lockTimer:
                        lockTimer += LOCK_LIMIT
                        diffPixels(targetPL, 'target miss:\n')
                        alert()
                    else:
                        if checkPixels(whilePL):
                            rClick(*clickInfo)
                            wait(retryDelay, 0.2)
                            retries += 1
                            if retries > RETRY_LIMIT:
                                wait(10, 0)
        else:
            rClick(*clickInfo)
            wait(conditionWait, 0.2)
            if not checkPixels(targetPL):
                # Do initial wait before actually retrying, condition wait is only how long it should usually take
                wait(retryDelay, 0.2)
                while not checkPixels(targetPL):
                    wait(0.04)
                    if time.clock() > lockTimer:
                        lockTimer += LOCK_LIMIT
                        diffPixels(targetPL, 'target miss:\n')
                        alert()
                    else:
                        rClick(*clickInfo)
                        wait(retryDelay, 0.2)
                        retries += 1
                        if retries > RETRY_LIMIT:
                            wait(10, 0)

#sequence lists:
#[PL,action,PL,action.....PL]
#a list of states and transition actions interlocked
#terminating with a final state
#Not manditory usage, but probably saves some trouble
#PL: a state array
#action: (clickInfo, conditionWait, retryDelay, drag)
#clickInfo: either in form (pos, dev, r) as a normal click or (p1, p4, r, time) as a drag
#drag is just boolean
def runSequence(s):
    for i in range(0, len(s)-2, 2):
        while not cd.MAP_RUNNING and not cd.DEBUG_RUNNING:
            wait(0.1, 0)
        ap = s[i+1]
        actionUntil(s[i+2], ap[0], ap[1], ap[2], s[i], ap[3])

#read the screen when logistics tab is opened and discerns the time remaining on all 4 logistics
#be in the main screen with either the logistics tab open or not (it'll close the tab after completion)
#no other timer should be active in this tab while this is running
#logiRegions are using top left corner (x,y,w,h) new screenshot uses bottom right instead of w,h
logiRegions = [(830,120,178,69), (830,233,178,69), (830,346,178,69), (830,459,178,69)]
mainScreenTabClose = [((277, 538), (255, 182, 0)), ((277, 149), (57, 195, 255)), ((1583, 60), (255, 182, 0)), ((1583, 1014), (255, 255, 255))]
mainScreenTabOpen = [((462, 130), (255, 182, 0)), ((463, 242), (255, 182, 0)), ((462, 356), (255, 182, 0)), ((462, 468), (255, 182, 0)), ((769, 157), (49, 36, 0)), ((773, 269), (49, 36, 0)), ((771, 381), (49, 36, 0)), ((772, 495), (49, 36, 0)), ((1073, 540), (255, 182, 0))]
openLogiTab = ((292, 538), (17.0, 36.5), 0)
closeLogiTab = ((1063, 539), (22.5, 35.5), 0)

def logiSync():
    logiTabActive()
    for i in range(4):
        reg = logiRegions[i]
        convertedRegion = (reg[0] + cd.winX, reg[1] + cd.winY, reg[0] + cd.winX + reg[2], reg[1] + cd.winY + reg[3])
        remaining = getTimer(getScreenText(convertedRegion))
        while remaining == None:
            logiTabActive()
            remaining = getTimer(getScreenText(convertedRegion))
        cd.logiCountdown[i] = round(time.time() + remaining)
    logiTabDeactive()

#open the tab if it detect the main screen instead
def logiTabActive():
    actionUntil(mainScreenTabOpen, openLogiTab, 1, 1, mainScreenTabClose)

#close the tab
def logiTabDeactive():
    actionUntil(mainScreenTabClose, closeLogiTab, 1, 1, mainScreenTabOpen)