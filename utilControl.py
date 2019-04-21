from utilContext import *
from utilPrimitive import *

DRAG_TIME_STEP = 0.005          # time to wait during drag move

#mean is the center point, deviance defines a rectangle range for 3.5 standard deviations
#defining r will constrain the click areas with given radius
def rClick(mean, dev, r = 0):
    click(randPoint(mean, dev, r))
    wait(0.001, 0)

#creates a 4 point bezier drag path
#point are at 0, 0.333, 0.666, 1 along the length
#middle 2 points will be randomized with r defining a circular radius
#delta is time take to complete drag
def rDrag(p1, p4, r = 0, time = 0.5):
    p2 = randPoint(midPoint(p1, p4, 1/3), (r, r), r)
    p3 = randPoint(midPoint(p1, p4, 2/3), (r, r), r)
    mouseTo(p1)
    mouseDown()
    t = 0
    while t < time:
        wait(DRAG_TIME_STEP, 0)
        t = min(t + normalRange(DRAG_TIME_STEP, DRAG_TIME_STEP/2), time)
        mouseMove(cubicBezier(p1, p2, p3, p4, t/time))
    mouseUp()

#Does a small amount of holding down before actually moving
def rHoldDrag(p1, p4, r = 0, time = 0.5, hold = 0.01):
    p2 = randPoint(midPoint(p1, p4, 1/3), (r, r), r)
    p3 = randPoint(midPoint(p1, p4, 2/3), (r, r), r)
    mouseTo(p1)
    mouseDown()
    wait(hold, 0)
    t = 0
    while t < time:
        wait(DRAG_TIME_STEP, 0)
        t = min(t + normalRange(DRAG_TIME_STEP, DRAG_TIME_STEP/2), time)
        mouseMove(cubicBezier(p1, p2, p3, p4, t/time))
    wait(hold, 0)
    mouseUp()