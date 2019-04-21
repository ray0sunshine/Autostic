import time

from utilControl import *
from utilInformation import *
from utilContext import *
from utilMovement import *

from driver43e import *

def testColorPerformance():
    t1 = time.time()
    for _ in range(100000):
        #print(getMouseColor())
        getMouseColor()
    t2 = time.time()
    print(t2 - t1)

def testClick():
    for _ in range(3000):
        rClick((500,500), (200,100), 100)

def quickTest():
    filterAR54StarP2()
    pass

def getMouseColorTest():
    print('MousePos:', getMousePos(), 'Color:', getMouseColor())

def varyDrag():
    rDrag(randPoint((800,250),(200,100)), randPoint((800,850),(120,100)), 300, 0.02)

def testAll():
    rClick(*pos9)
    rClick(*pos8)
    rClick(*pos7)
    rClick(*pos6)
    rClick(*pos5)
    rClick(*pos4)
    rClick(*pos3)
    rClick(*pos2)
    rClick(*pos1)
    rClick(*skill1)
    rClick(*skill2)
    rClick(*skill3)
    rClick(*skill4)
    rClick(*skill5)
    rClick(*autoSkill)
    rClick(*withdraw)

def multiTestAll():
    for _ in range(100):
        testAll()