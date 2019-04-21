import keyboard as key
import sys

from utilContext import *
from utilDriver import *
from utilTest import *
from utilDisplay import *
from utilLogistic import *
from utilManagement import *
from utilConfig import *
from utilMovement import *

from driver02 import *

loadConfig()
initContext('NoxPlayer')
initUI()
initLogi()
initRun()

key_suppress = False

key.add_hotkey('f1', clearReferencePixel, suppress=key_suppress)           #clear stack
key.add_hotkey('f2', removeLastReferencePixel, suppress=key_suppress)      #pop last reference pixel
key.add_hotkey('f3', addReferencePixel, suppress=key_suppress)             #push new reference pixel to stack
key.add_hotkey('f4', copyPLToClipBoard, suppress=key_suppress)             #screen state array

key.add_hotkey('f5', getCircularClick, suppress=key_suppress)              #circular click setting
key.add_hotkey('f6', getRectClick, suppress=key_suppress)                  #rectangle click setting
key.add_hotkey('f7', decrementRun, suppress=key_suppress)                  #-1 cycle
key.add_hotkey('f8', incrementRun, suppress=key_suppress)                  #+1 cycle

key.add_hotkey('f9', kill, suppress=key_suppress)                          #dishonorable death
key.add_hotkey('f10', threadRun, suppress=key_suppress)                    #start/pause running
key.add_hotkey('f11', toggleFirstOrder, suppress=key_suppress)             #toggle dragger order
key.add_hotkey('f12', toggleLogi, suppress=key_suppress)                   #toggle logistics

key.add_hotkey('ctrl+f1', login, suppress=key_suppress)                    #login using config user and pass
key.add_hotkey('ctrl+f2', multiTestAll, suppress=key_suppress)             #try pressing all buttons
key.add_hotkey('ctrl+f3', decrementLogiWait, suppress=key_suppress)        #-1 logistics to wait for
key.add_hotkey('ctrl+f4', incrementLogiWait, suppress=key_suppress)        #+1 logistics to wait for

key.add_hotkey('ctrl+f5', decrementRepair, suppress=key_suppress)          #test management
key.add_hotkey('ctrl+f6', incrementRepair, suppress=key_suppress)          #test alert
key.add_hotkey('ctrl+f7', decrementBurn, suppress=key_suppress)            #-1 big cycle
key.add_hotkey('ctrl+f8', incrementBurn, suppress=key_suppress)            #+1 big cycle

key.add_hotkey('ctrl+f10', resetProgress, suppress=key_suppress)           #reset runs and cycles to 0
key.add_hotkey('ctrl+f11', testColorPerformance, suppress=key_suppress)    #performance test
key.add_hotkey('ctrl+f12', logiSync, suppress=key_suppress)                #get times for logi

key.add_hotkey('8', mouseShift, args=(0,-1))  #up
key.add_hotkey('4', mouseShift, args=(-1,0))  #left
key.add_hotkey('6', mouseShift, args=(1,0))   #right
key.add_hotkey('2', mouseShift, args=(0,1))   #down

#print(key.read_key())
key.wait('esc')