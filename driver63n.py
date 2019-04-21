import random
import threading
import time

from utilDriver import *
from utilPrimitive import *
from utilContext import *
from utilManagement import *
from utilMovement import *

grid_radius = 15

posGrid = []
posGrid.append((None))
posGrid.append(((342, 714), (grid_radius, grid_radius), grid_radius))
posGrid.append(((559, 727), (grid_radius, grid_radius), grid_radius))
posGrid.append(((794, 728), (grid_radius, grid_radius), grid_radius))
posGrid.append(((443, 577), (grid_radius, grid_radius), grid_radius))
posGrid.append(((633, 577), (grid_radius, grid_radius), grid_radius))
posGrid.append(((824, 576), (grid_radius, grid_radius), grid_radius))
posGrid.append(((524, 475), (grid_radius, grid_radius), grid_radius))
posGrid.append(((682, 476), (grid_radius, grid_radius), grid_radius))
posGrid.append(((842, 476), (grid_radius, grid_radius), grid_radius))

PL_mainMenu = [((277, 150), (57, 195, 255)), ((277, 538), (255, 182, 0)), ((1582, 1013), (255, 255, 255)), ((1583, 60), (255, 182, 0))]
PL_ch6nm = [((494, 828), (255, 182, 0)), ((493, 717), (255, 255, 255)), ((1440, 153), (255, 182, 0))]
night = (((1544, 222), (42.0, 22.0), 0), 0.5, 0.3, False)
PL_ch6ntm = [((1438, 154), (16, 77, 99)), ((496, 826), (255, 182, 0)), ((492, 712), (255, 255, 255))]
mission = (((1198, 570), (292.0, 45.0), 0), 0.5, 0.3, False)
PL_mission = [((776, 769), (140, 199, 24)), ((1028, 779), (255, 182, 0)), ((546, 402), (255, 255, 255)), ((530, 262), (255, 255, 255))]
battle = (((1050, 766), (74.0, 32.5), 0), 3, 3, False)
PL_map1 = [((1141, 564), (206, 0, 0)), ((1470, 335), (181, 190, 206)), ((571, 498), (206, 0, 0)), ((806, 511), (206, 0, 0)), ((1531, 811), (206, 0, 0))]

click_command = (((959, 539), (54, 54), 54), 1, 1, False)
click_heli = (((760, 338), (39, 39), 39), 1, 1, False)
click_heli_dshort = (((760, 338), (39, 39), 39), 0.5, 0.5, False)
click_heli2 = (((991, 470), (40, 40), 40), 1, 1, False)
click_heli2_dshort = (((991, 470), (40, 40), 40), 0.5, 0.5, False)
PL_echChoose = [((1542, 312), (0, 48, 66)), ((1542, 322), (16, 101, 140)), ((439, 245), (255, 255, 255)), ((457, 800), (255, 117, 0)), ((1467, 852), (49, 48, 49)), ((1427, 868), (255, 186, 0))]
ech_formation = (((522, 812), (78.0, 17.0), 0), 1, 1, False)
PL_ech1 = [((291, 51), (255, 255, 255)), ((382, 216), (255, 182, 0)), ((384, 308), (255, 255, 255)), ((1412, 802), (255, 255, 255)), ((1437, 789), (49, 48, 49))]
dps1 = (((705, 515), (73.5, 157.5), 0), 1, 0.3, False)
PL_dollSelect = [((293, 52), (255, 255, 255)), ((1569, 170), (49, 48, 49)), ((1554, 183), (255, 255, 255)), ((1569, 298), (49, 48, 49)), ((1551, 313), (255, 255, 255)), ((1213, 457), (239, 239, 239))]
filterBy = (((1510, 329), (78.0, 44.0), 0), 0.5, 0.3, False)
PL_filter = [((1138, 746), (255, 162, 0)), ((1071, 743), (255, 255, 255)), ((943, 521), (255, 255, 255)), ((1289, 464), (255, 255, 255))]

formation_preset = (((1491, 864), (74.0, 23.0), 0), 0.6, 0.3, False)
PL_formation_preset = [((1300, 786), (255, 255, 255)), ((1490, 790), (255, 182, 0)), ((1579, 439), (255, 125, 0))]
presets = (((1570, 447), (32.5, 37.0), 0), 0.6, 0.3, False)
PL_presets = [((987, 540), (255, 138, 0)), ((1567, 922), (206, 101, 0)), ((1300, 922), (206, 203, 206))]
preset1 = (((1307, 110), (263.5, 46.0), 0), 0.6, 0.3, False)
preset2 = (((1307, 239), (260.5, 44.5), 0), 0.6, 0.3, False)
preset3 = (((1307, 367), (261.5, 44.5), 0), 0.6, 0.3, False)
preset4 = (((1307, 496), (261.5, 44.5), 0), 0.6, 0.3, False)
PL_preset1 = [((1024, 109), (255, 125, 0))]
PL_preset2 = [((1024, 239), (255, 125, 0))]
PL_preset3 = [((1024, 367), (255, 125, 0))]
PL_preset4 = [((1024, 496), (255, 125, 0))]
preset_use = (((1458, 958), (109.5, 36.5), 0), 0.6, 0.3, False)
PL_prompt = [((748, 663), (255, 255, 255)), ((1130, 709), (255, 182, 0)), ((1296, 923), (132, 134, 132)), ((1565, 924), (140, 69, 0))]
PL_prompt_force = [((795, 581), (255, 186, 0)), ((833, 619), (255, 186, 0))]
PL_prompt_not_force = [((833, 581), (255, 255, 255)), ((795, 619), (255, 255, 255))]
preset_force = (((814, 600), (20.0, 19.0), 0), 0.6, 0.3, False)
preset_force_confirm = (((1130, 685), (76.5, 22.0), 0), 0.6, 0.3, False)
preset_ok = (((1489, 826), (74.5, 42.5), 0), 0.6, 0.3, False)

arSelect = (((917, 540), (78.0, 29.5), 0), 0.5, 0.3, False)
rfSelect = (((1296, 446), (79.0, 29.5), 0), 0.5, 0.3, False)
PL_arOnly = [((948, 520), (255, 182, 0)), ((1136, 744), (255, 162, 0)), ((1570, 298), (49, 48, 49)), ((1550, 310), (255, 255, 255))]
confirmFilter = (((1250, 745), (124.0, 20.0), 0), 1.3, 0.3, False)
PL_filtered = [((633, 159), (255, 186, 0)), ((1441, 355), (255, 182, 0)), ((1213, 458), (239, 239, 239)), ((1570, 298), (49, 48, 49)), ((1552, 315), (255, 255, 255)), ((1569, 169), (49, 48, 49)), ((1549, 179), (255, 255, 255))]

ech2Select = (((329, 308), (50.5, 27.0), 0), 1.15, 0.3, False)
PL_ech2 = [((291, 51), (255, 255, 255)), ((385, 311), (255, 182, 0)), ((383, 215), (255, 255, 255)), ((1542, 331), (0, 48, 66)), ((1532, 341), (49, 48, 49))]
dps2Select = (((514, 513), (76.5, 155.0), 0), 1, 0.3, False)
backMap = (((341, 79), (58.0, 36.0), 0), 3, 0.3, False)

deployOk = (((1507, 841), (76.5, 22.0), 0), 0.5, 0.3, False)
startMap = (((1458, 979), (130.5, 42.5), 0), 6, 6, False)
PL_mapStarted = [((419, 920), (255, 255, 255)), ((1469, 334), (181, 190, 206)), ((1140, 565), (206, 0, 0))]
PL_resupply = [((441, 244), (255, 255, 255)), ((456, 800), (255, 117, 0)), ((1541, 312), (0, 48, 66)), ((1542, 321), (16, 101, 140)), ((1543, 771), (239, 207, 0)), ((1456, 855), (49, 48, 49))]
resupply = (((1507, 748), (92.0, 21.5), 0), 0.8, 0.3, False)

planning = (((345, 913), (69.0, 18.0), 0), 1, 0.3, False)
PL_planning = [((412, 905), (251, 207, 76))]
PL_commandSelected = [((817, 321), (255, 186, 0)), ((703, 321), (255, 186, 0)), ((760, 257), (255, 186, 0))]
PL_dragged = [((582, 62), (255, 85, 0)), ((440, 980), (255, 0, 0)), ((1394, 526), (255, 255, 255)), ((1124, 519), (255, 255, 255)), ((1122, 798), (255, 255, 255)), ((1139, 302), (255, 0, 0))]

node1 = (((1076, 370), (32, 32), 32), 0.3, 0.3, False)
node2 = (((1327, 359), (30, 30), 30), 0.3, 0.3, False)
PL_n1 = [((1115, 349), (255, 187, 0))]
PL_n2 = [((1289, 340), (255, 186, 0))]
execute = (((1513, 981), (76.5, 34.5), 0), 0.5, 0.3, False)
PL_executed = [((273, 914), (1, 1, 1))]

PL_battle = [((930, 48), (255, 186, 0)), ((937, 48), (255, 255, 255)), ((941, 48), (255, 186, 0)), ((946, 48), (255, 255, 255)), ((954, 48), (255, 186, 0))]
PL_ended = [((342, 499), (206, 0, 0)), ((415, 831), (206, 0, 0)), ((1301, 810), (206, 0, 0))]
endRound = (((1502, 984), (75.5, 34.0), 0), 24, 24, False)
endRound2 = (((1502, 984), (75.5, 34.0), 0), 10, 10, False)

PL_turn2 = [((340, 499), (206, 0, 0)), ((415, 830), (206, 0, 0)), ((991, 454), (123, 174, 239))]
PL_node4 = [((757, 285), (255, 186, 0)), ((818, 216), (255, 186, 0))]
node5 = (((1118, 300), (29, 29), 29), 0.3, 0.3, False)
node6 = (((1311, 339), (53, 53), 53), 0.8, 0.3, False)
PL_n5 = [((1077, 317), (255, 186, 0))]
PL_n6 = [((1326, 384), (255, 186, 0))]

# swap
PL_swap_selected = [((1434, 451), (237, 168, 0))]
swap_node = (((1101, 360), (28, 28), 28), 1, 1, False)
PL_swap_node = [((1179, 347), (255, 213, 0)), ((1024, 345), (255, 214, 0))]
switch = (((994, 360), (68.0, 20.0), 0), 1, 1, False)
PL_swapped = [((986, 347), (255, 0, 0)), ((1099, 277), (255, 186, 0))]
PL_retreat_selected = [((917, 455), (255, 212, 0)), ((1071, 457), (255, 216, 0))]
select_retreat = (((1093, 472), (66.5, 20.0), 0), 1, 1, False)
PL_retreat_target = [((990, 139), (236, 168, 0))]
retreat = (((1316, 841), (76.5, 23.5), 0), 0.7, 0.3, False)
PL_confirm_retreat = [((1069, 667), (255, 223, 0)), ((845, 664), (255, 255, 255))]
confirm_retreat = (((1053, 679), (78.0, 24.5), 0), 0.7, 0.3, False)
begin_terminate = (((602, 75), (45.0, 29.5), 0), 0.7, 0.3, False)
PL_terminating = [((845, 680), (222, 48, 49)), ((1031, 682), (255, 138, 49))]
restart_mission = (((783, 676), (72.0, 19.5), 0), 0.7, 0.3, False)
terminate_mission = (((1099, 676), (72.5, 21.0), 0), 0.7, 0.3, False)

# comes later
PL_ended2 = [((582, 60), (255, 85, 0)), ((818, 302), (148, 203, 255)), ((1120, 302), (255, 0, 0)), ((1393, 513), (255, 0, 0)), ((1388, 999), (255, 170, 0)), ((1359, 999), (255, 170, 0))]
PL_result = [((1581, 69), (255, 219, 107)), ((1594, 52), (255, 186, 99)), ((465, 793), (239, 169, 0)), ((406, 735), (252, 197, 3)), ((363, 494), (255, 255, 255))]

#Manually ran
clickAway = ((995, 586), (313.5, 217.5), 0)
clickToMainMenu = ((359, 246), (68.5, 21.5), 0)
clickToChapters = (((1239, 717), (96.0, 36.0), 0), 3, 3, False)
PL_loading = [((1072, 275), (66, 69, 66)), ((724, 282), (66, 69, 66)), ((903, 281), (66, 69, 66)), ((803, 395), (198, 195, 198)), ((886, 439), (198, 195, 198)), ((956, 487), (198, 195, 198))]

#specifically set filters up
#future additions can include more diverse combinations
def filterAR():
    runSequence([PL_filter, arSelect, PL_arOnly, confirmFilter, PL_filtered])

def randomMapDrag():
    return ((randPoint((1142, 202), (200, 120)), randPoint((1202, 797), (250, 100)), 150, normalRange(0.45, 0.15)), 0.5, 0.5, True)

def initRun():
    cycle = threading.Thread(None, run, 'run')
    cycle.start()

def threadRun():
    # only reset if ended a run
    if cd.runsDone == cd.runsLimit:
        cd.runsDone = 0

    # can manually set logistics to wait for (delayed start)
    if cd.runsDone == 0:
        doLogistics()

    cd.MAP_RUNNING = not cd.MAP_RUNNING

def run():
    while not cd.COMMIT_SUDOKU:
        if cd.runsDone == 0 and cd.MAP_RUNNING:
            cd.RUNTIME = time.time()
        while cd.runsDone < cd.runsLimit and cd.MAP_RUNNING:
            runMap(cd.firstOrder)
            runMap(not cd.firstOrder)

        if cd.runsDone > 0:
            #probably need a thing to reset burnFodder
            if cd.burnFodder < cd.burnFodderLimit:
                burn_fodder(False)
                cd.burnFodder += 1
                cd.MAP_RUNNING = False
                threadRun()
            elif cd.MAP_RUNNING:
                alert()
                cd.MAP_RUNNING = False
        wait(0.1, 0)

def setTeams(firstOrder):
    if firstOrder:
        runSequence([PL_presets, preset2, PL_preset2, preset_use, PL_prompt])
        if checkPixels(PL_prompt_not_force):
            runSequence([PL_prompt_not_force, preset_force, PL_prompt_force])
        runSequence([PL_prompt_force, preset_force_confirm, PL_formation_preset, preset_ok, PL_ech1, ech2Select, PL_ech2])
        runSequence([PL_ech2, formation_preset, PL_formation_preset, presets, PL_presets])
        runSequence([PL_presets, preset4, PL_preset4, preset_use, PL_prompt])
        if checkPixels(PL_prompt_not_force):
            runSequence([PL_prompt_not_force, preset_force, PL_prompt_force])
        runSequence([PL_prompt_force, preset_force_confirm, PL_formation_preset, preset_ok, PL_ech2, backMap, PL_map1])
    else:
        runSequence([PL_presets, preset1, PL_preset1, preset_use, PL_prompt])
        if checkPixels(PL_prompt_not_force):
            runSequence([PL_prompt_not_force, preset_force, PL_prompt_force])
        runSequence([PL_prompt_force, preset_force_confirm, PL_formation_preset, preset_ok, PL_ech1, ech2Select, PL_ech2])
        runSequence([PL_ech2, formation_preset, PL_formation_preset, presets, PL_presets])
        runSequence([PL_presets, preset3, PL_preset3, preset_use, PL_prompt])
        if checkPixels(PL_prompt_not_force):
            runSequence([PL_prompt_not_force, preset_force, PL_prompt_force])
        runSequence([PL_prompt_force, preset_force_confirm, PL_formation_preset, preset_ok, PL_ech2, backMap, PL_map1])

def runMap(firstOrder):
    # just restart in map
    if not checkPixels(PL_map1):
        #wait until one of the start conditions is met before running through sequences
        starterWait = 0
        while not checkPixels(PL_mainMenu) and not checkPixels(PL_ch6nm):
            starterWait += 1
            if starterWait > 15:
                starterWait = 0
                alert()
            wait(1)

        #if starting from main menu
        if checkPixels(PL_mainMenu):
            logiSync()
            runSequence([PL_mainMenu, clickToChapters, PL_ch6nm])

        #enter map
        runSequence([PL_ch6nm, night, PL_ch6ntm, mission, PL_mission, battle, PL_map1])

    #setup echelons and filter
    runSequence([PL_map1, click_heli, PL_echChoose, ech_formation, PL_ech1, formation_preset, PL_formation_preset, presets, PL_presets])

    #set the teams
    setTeams(firstOrder)

    #deploy on heli and cmd
    runSequence([PL_map1, click_heli, PL_echChoose, deployOk, PL_map1])

    #start, resupply, planning, select heli, scroll
    runSequence([PL_map1, startMap, PL_mapStarted, click_heli_dshort, PL_commandSelected, planning, PL_planning])

    #select 2 nodes
    runSequence([PL_planning, node1, PL_n1, node2, PL_n2])

    #execute
    runSequence([PL_n2, execute, PL_executed])

    #wait loop
    for i in range(2):
        singularFight(i)

    #end turn
    runSequence([PL_ended, endRound, PL_turn2, click_heli2, PL_echChoose, deployOk, PL_ended])

    #swap and retreat
    runSequence([PL_ended, click_heli2, PL_swap_selected, swap_node, PL_swap_node, switch, PL_swapped, click_heli2, PL_retreat_selected, select_retreat, PL_retreat_target, click_heli2, PL_resupply, retreat, PL_confirm_retreat])

    #confirm and restart
    runSequence([PL_confirm_retreat, confirm_retreat, PL_ended, begin_terminate, PL_terminating, restart_mission, PL_map1])

    ###
    # Restart and run again
    ###

    #deploy on heli and cmd
    runSequence([PL_map1, click_heli, PL_echChoose, deployOk, PL_map1])

    #start, resupply, planning, select heli, scroll
    runSequence([PL_map1, startMap, PL_mapStarted, click_heli_dshort, PL_commandSelected, planning, PL_planning])

    #select 2 nodes
    runSequence([PL_planning, node1, PL_n1, node2, PL_n2])

    #execute
    runSequence([PL_n2, execute, PL_executed])

    #wait loop
    for i in range(2):
        singularFight(i)

    #end turn
    runSequence([PL_ended, endRound, PL_turn2, click_heli2, PL_echChoose, deployOk, PL_ended])

    #resupply and retreat
    runSequence([PL_ended, click_heli2_dshort, PL_swap_selected, click_heli2_dshort, PL_resupply, resupply, PL_ended, click_heli2_dshort, PL_resupply, retreat, PL_confirm_retreat])

    #click through, exit to main menu if at end of script
    if cd.runsDone < cd.runsLimit:
        runSequence([PL_confirm_retreat, confirm_retreat, PL_ended, begin_terminate, PL_terminating, restart_mission, PL_map1])
    else:
        runSequence([PL_confirm_retreat, confirm_retreat, PL_ended, begin_terminate, PL_terminating, terminate_mission, PL_mainMenu])

def singularFight(index):
    while not checkPixels(PL_battle):
        wait(0.05, 0)
    micro(index)
    while checkPixels(PL_battle):
        wait(0.05, 0)
    cd.runsDone = round(cd.runsDone + 0.125, 3)
    wait(2.3, 0.2)
    rpt = randPoint(*clickAway)

    maxLim = 150
    rclicks_count = 0
    while not checkPixels(PL_loading):
        rClick(rpt, (40, 40), 40)
        wait(0.18, 0.03)
        rclicks_count += 1
        if rclicks_count > maxLim:
            return

def micro(index):
    #do some kiting here (maybe per fight based on index?)
    wait(0.5, 0.2)

def testRun():
    #param = ((1248, 735), (104.5, 36.0), 0)
    for _ in range(10):
        #rClick(*param)
        rDrag(*(randPoint((1142, 202), (200, 120)), randPoint((1202, 797), (250, 100)), 150, 0.2))
