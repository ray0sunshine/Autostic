import keyboard as key
import sys

from collections import deque
from utilContext import *
from utilTest import *
from utilMovement import *

grid_radius = 15

pos9 = ((842, 476), (grid_radius, grid_radius), grid_radius)
pos8 = ((682, 476), (grid_radius, grid_radius), grid_radius)
pos7 = ((524, 475), (grid_radius, grid_radius), grid_radius)
pos6 = ((824, 576), (grid_radius, grid_radius), grid_radius)
pos5 = ((633, 577), (grid_radius, grid_radius), grid_radius)
pos4 = ((443, 577), (grid_radius, grid_radius), grid_radius)
pos3 = ((794, 728), (grid_radius, grid_radius), grid_radius)
pos2 = ((559, 727), (grid_radius, grid_radius), grid_radius)
pos1 = ((342, 714), (grid_radius, grid_radius), grid_radius)

skill1 = ((570, 985), (45, 45), 45)
skill2 = ((769, 984), (45, 45), 45)
skill3 = ((967, 983), (47, 47), 47)
skill4 = ((1166, 983), (47, 47), 47)
skill5 = ((1365, 985), (50, 50), 50)

initContext('NoxPlayer')

#key.add_hotkey('9', positionSelected, args=pos9, suppress=True)
#key.add_hotkey('8', positionSelected, args=pos8, suppress=True)
#key.add_hotkey('7', positionSelected, args=pos7, suppress=True)
#key.add_hotkey('6', positionSelected, args=pos6, suppress=True)
#key.add_hotkey('5', positionSelected, args=pos5, suppress=True)
#key.add_hotkey('4', positionSelected, args=pos4, suppress=True)
#key.add_hotkey('3', positionSelected, args=pos3, suppress=True)
#key.add_hotkey('2', positionSelected, args=pos2, suppress=True)
#key.add_hotkey('1', positionSelected, args=pos1, suppress=True)

#key.add_hotkey('alt+9', positionSwapped, args=pos9, suppress=True)
#key.add_hotkey('alt+8', positionSwapped, args=pos8, suppress=True)
#key.add_hotkey('alt+7', positionSwapped, args=pos7, suppress=True)
#key.add_hotkey('alt+6', positionSwapped, args=pos6, suppress=True)
#key.add_hotkey('alt+5', positionSwapped, args=pos5, suppress=True)
#key.add_hotkey('alt+4', positionSwapped, args=pos4, suppress=True)
#key.add_hotkey('alt+3', positionSwapped, args=pos3, suppress=True)
#key.add_hotkey('alt+2', positionSwapped, args=pos2, suppress=True)
#key.add_hotkey('alt+1', positionSwapped, args=pos1, suppress=True)

#key.add_hotkey('ctrl+9', positionWalked, args=pos9, suppress=True)
#key.add_hotkey('ctrl+8', positionWalked, args=pos8, suppress=True)
#key.add_hotkey('ctrl+7', positionWalked, args=pos7, suppress=True)
#key.add_hotkey('ctrl+6', positionWalked, args=pos6, suppress=True)
#key.add_hotkey('ctrl+5', positionWalked, args=pos5, suppress=True)
#key.add_hotkey('ctrl+4', positionWalked, args=pos4, suppress=True)
#key.add_hotkey('ctrl+3', positionWalked, args=pos3, suppress=True)
#key.add_hotkey('ctrl+2', positionWalked, args=pos2, suppress=True)
#key.add_hotkey('ctrl+1', positionWalked, args=pos1, suppress=True)

# alt to do predetermined double swaps (animation cancel mg)

#key.add_hotkey('z', skill, args=skill1)
#key.add_hotkey('x', skill, args=skill2)
#key.add_hotkey('c', skill, args=skill3)
#key.add_hotkey('v', skill, args=skill4)
#key.add_hotkey('b', skill, args=skill5)

#key.add_hotkey('0', withdraw)
key.add_hotkey('z', withdrawManual)
key.add_hotkey('x', pause)
#key.add_hotkey('+', reverseSwap)
#key.add_hotkey('-', autoToggle)
#key.add_hotkey(' ', resetScreen)

#key.add_hotkey('f9', kill)

#key.on_release_key('shift', clearPositionQueue)
#key.on_release_key('ctrl', clearPositionQueue)

executeMoverThread()
key.wait('f9')