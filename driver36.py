import random
import threading
import time

from utilDriver import *
from utilControl import *
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
PL_ch4nm = [((496, 504), (255, 182, 0)), ((493, 394), (255, 255, 255)), ((494, 608), (255, 255, 255)), ((1409, 152), (255, 182, 0))]
emergency = (((1424, 222), (50.0, 30.0), 0), 0.5, 0.3, False)
PL_ch4em = [((1423, 155), (231, 52, 0)), ((497, 611), (255, 182, 0)), ((287, 46), (255, 186, 0)), ((1452, 586), (49, 48, 49))]
mission = (((1087, 943), (211.5, 37.5), 0), 0.5, 0.3, False)
PL_mission = [((1028, 777), (255, 182, 0)), ((524, 259), (255, 255, 255))]
battle = (((1050, 766), (74.0, 32.5), 0), 3, 3, False)
PL_map1 = [((885, 199), (255, 255, 255)), ((622, 292), (255, 255, 255)), ((717, 225), (49, 83, 33)), ((995, 543), (231, 231, 181))]

click_heli = (((1379, 269), (36, 36), 36), 1, 1, False)
click_command = (((1022, 396), (22, 22), 22), 0.5, 1, False)
click_command_dshort = (((1022, 396), (22, 22), 22), 0.2, 0.3, False)
PL_echChoose = [((1542, 312), (0, 48, 66)), ((1542, 322), (16, 101, 140)), ((439, 245), (255, 255, 255)), ((457, 800), (255, 117, 0)), ((1467, 852), (49, 48, 49)), ((1427, 868), (255, 186, 0))]
ech_formation = (((522, 812), (78.0, 17.0), 0), 1, 1, False)
PL_ech1 = [((291, 51), (255, 255, 255)), ((382, 216), (255, 182, 0)), ((384, 308), (255, 255, 255)), ((1412, 802), (255, 255, 255)), ((1437, 789), (49, 48, 49))]
dps1 = (((705, 515), (73.5, 157.5), 0), 1, 0.3, False)
PL_dollSelect = [((293, 52), (255, 255, 255)), ((1569, 170), (49, 48, 49)), ((1554, 183), (255, 255, 255)), ((1569, 298), (49, 48, 49)), ((1551, 313), (255, 255, 255)), ((1213, 457), (239, 239, 239))]
filterBy = (((1510, 329), (78.0, 44.0), 0), 0.5, 0.3, False)
PL_filter = [((1138, 746), (255, 162, 0)), ((1071, 743), (255, 255, 255)), ((943, 521), (255, 255, 255)), ((1289, 464), (255, 255, 255))]

arSelect = (((917, 540), (78.0, 29.5), 0), 0.5, 0.3, False)
rfSelect = (((1296, 446), (79.0, 29.5), 0), 0.5, 0.3, False)
mgSelect = (((1110, 541), (75.5, 19.5), 0), 0.5, 0.3, False)
star5 = (((916, 220), (78.5, 29.5), 0), 0.5, 0.3, False)
PL_star5 = [((936, 199), (255, 182, 0))]
star4 = (((1106, 221), (77.0, 29.0), 0), 0.5, 0.3, False)
PL_star4 = [((1125, 205), (255, 182, 0))]
PL_arOnly = [((948, 520), (255, 182, 0)), ((1136, 744), (255, 162, 0)), ((1570, 298), (49, 48, 49)), ((1550, 310), (255, 255, 255))]
PL_rfOnly = [((1283, 464), (255, 182, 0)), ((948, 521), (255, 255, 255)), ((1065, 742), (255, 255, 255)), ((1143, 743), (255, 162, 0))]
PL_mgOnly = [((1140, 516), (255, 182, 0)), ((1312, 517), (255, 255, 255)), ((936, 519), (255, 255, 255)), ((1263, 461), (255, 255, 255))]
confirmFilter = (((1250, 745), (124.0, 20.0), 0), 1.3, 0.3, False)
PL_filtered = [((633, 159), (255, 186, 0)), ((1441, 355), (255, 182, 0)), ((1213, 458), (239, 239, 239)), ((1570, 298), (49, 48, 49)), ((1552, 315), (255, 255, 255)), ((1569, 169), (49, 48, 49)), ((1549, 179), (255, 255, 255))]
PL_filtered_p2 = [((445, 431), (255, 186, 0)), ((1441, 355), (255, 182, 0)), ((1213, 458), (239, 239, 239)), ((1570, 298), (49, 48, 49)), ((1552, 315), (255, 255, 255)), ((1569, 169), (49, 48, 49)), ((1549, 179), (255, 255, 255))]

ech2Select = (((329, 308), (50.5, 27.0), 0), 1.15, 0.3, False)
PL_ech2 = [((291, 51), (255, 255, 255)), ((385, 311), (255, 182, 0)), ((383, 215), (255, 255, 255)), ((1542, 331), (0, 48, 66)), ((1532, 341), (49, 48, 49))]
dps2Select = (((514, 513), (76.5, 155.0), 0), 1, 0.3, False)
backMap = (((341, 79), (58.0, 36.0), 0), 3, 0.3, False)

deployOk = (((1507, 841), (76.5, 22.0), 0), 1, 0.3, False)
startMap = (((1458, 979), (130.5, 42.5), 0), 3.5, 15, False)
PL_mapStarted = [((276, 897), (255, 255, 255)), ((1339, 978), (255, 170, 0)), ((862, 410), (255, 255, 255)), ((405, 247), (41, 75, 24))]
PL_resupply = [((441, 244), (255, 255, 255)), ((456, 800), (255, 117, 0)), ((1541, 312), (0, 48, 66)), ((1542, 321), (16, 101, 140)), ((1543, 771), (239, 207, 0)), ((1456, 855), (49, 48, 49))]
resupply = (((1507, 748), (92.0, 21.5), 0), 0.8, 0.3, False)

planning = (((345, 913), (69.0, 18.0), 0), 1, 0.3, False)
PL_planning = [((412, 905), (251, 207, 76))]
PL_heliSelected = [((1455, 688), (255, 186, 0)), ((1346, 688), (255, 186, 0)), ((1400, 631), (255, 186, 0)), ((1400, 734), (255, 186, 0))]
PL_dragged = [((472, 819), (255, 255, 255)), ((965, 896), (0, 48, 74)), ((779, 658), (0, 52, 82)), ((1311, 408), (74, 69, 57)), ((1176, 790), (255, 0, 0))]

node1 = (((862, 410), (20, 20), 20), 0.4, 0.3, False)
node2 = (((948, 565), (21, 21), 21), 0.4, 0.3, False)
node3 = (((886, 704), (22, 22), 22), 0.4, 0.3, False)
node4 = (((813, 874), (36, 36), 36), 0.8, 0.3, False)
PL_n1 = [((861, 443), (255, 186, 0))]
PL_n2 = [((952, 597), (255, 186, 0))]
PL_n3 = [((892, 737), (255, 186, 0))]
PL_n4 = [((818, 906), (255, 186, 0))]
execute = (((1513, 981), (76.5, 34.5), 0), 0.5, 0.3, False)
PL_executed = [((275, 908), (49, 48, 49))]

PL_battle = [((930, 48), (255, 186, 0)), ((937, 48), (255, 255, 255)), ((941, 48), (255, 186, 0)), ((946, 48), (255, 255, 255)), ((954, 48), (255, 186, 0))]
PL_ended = [((863, 275), (255, 255, 255)), ((947, 430), (255, 0, 0)), ((885, 569), (255, 0, 0)), ((1161, 571), (16, 137, 110))]
endRound = (((1502, 984), (75.5, 34.0), 0), 9, 1, False)
PL_result = [((1595, 52), (255, 186, 99)), ((1573, 77), (255, 219, 107)), ((405, 790), (239, 107, 4)), ((460, 792), (197, 85, 3)), ((364, 494), (255, 255, 255))]

#Manually ran
clickAway = ((995, 586), (313.5, 217.5), 0)
clickToMainMenu = ((359, 246), (68.5, 21.5), 0)
clickToChapters = (((1239, 717), (96.0, 36.0), 0), 3, 3, False)
PL_loading = [((1072, 275), (66, 69, 66)), ((724, 282), (66, 69, 66)), ((903, 281), (66, 69, 66)), ((803, 395), (198, 195, 198)), ((886, 439), (198, 195, 198)), ((956, 487), (198, 195, 198))]

#specifically set filters up
#future additions can include more diverse combinations
#probably use a config for this lol
def filterAR():
    runSequence([PL_filter, arSelect, PL_arOnly, confirmFilter, PL_filtered])

def filterMG():
    runSequence([PL_filter, mgSelect, PL_mgOnly, confirmFilter, PL_filtered])

def filterAR54Star():
    runSequence([PL_filter, arSelect, PL_arOnly, star5, PL_star5, star4, PL_star4, confirmFilter, PL_filtered])

def filterAR54StarP2():
    runSequence([PL_filter, arSelect, PL_arOnly, star5, PL_star5, star4, PL_star4, confirmFilter, PL_filtered])
    wait(0.3, 0.1)
    rDrag(randPoint((1031, 916), (250, 69), 0), randPoint((1046, 230), (250, 69), 0), 150, 0.4)
    wait(0.3, 0.1)
    rDrag(randPoint((1031, 916), (250, 69), 0), randPoint((1046, 230), (250, 69), 0), 150, 0.4)
    wait(0.3, 0.1)

def filterRF54Star():
    runSequence([PL_filter, rfSelect, PL_rfOnly, star5, PL_star5, star4, PL_star4, confirmFilter, PL_filtered])
    
# make sure this doesn't touch a white node or it will cause a message to appear
def randomMapDrag():
    return ((randPoint((645, 202), (200, 120)), randPoint((700, 797), (250, 100)), 150, normalRange(0.45, 0.15)), 0.5, 0.5, True)

def initRun():
    cycle = threading.Thread(None, run, 'run')
    cycle.start()

def threadRun():
    #only reset if ended a run
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

        if cd.runsDone > 0:
            #probably need a thing to reset burnFodder
            if cd.burnFodder < cd.burnFodderLimit:
                burn_fodder()
                cd.burnFodder += 1
                cd.MAP_RUNNING = False
                threadRun()
            elif cd.MAP_RUNNING:
                alert()
                cd.MAP_RUNNING = False
        wait(0.1, 0)

def runMap(firstOrder):
    #wait until one of the start conditions is met before running through sequences
    starterWait = 0
    while not checkPixels(PL_mainMenu) and not checkPixels(PL_ch4nm):
        starterWait += 1
        if starterWait > 15:
            starterWait = 0
            alert()
        wait(1)

    #if starting from main menu
    if checkPixels(PL_mainMenu):
        logiSync()
        runSequence([PL_mainMenu, clickToChapters, PL_ch4nm])

    #enter map
    runSequence([PL_ch4nm, mission, PL_mission, battle, PL_map1])

    #deploy on heli and cmd
    runSequence([PL_map1, click_heli, PL_echChoose, deployOk, PL_map1, click_command, PL_echChoose, deployOk, PL_map1])

    #start, resupply, planning, select heli, scroll
    runSequence([PL_map1, startMap, PL_mapStarted, click_command_dshort, PL_mapStarted, click_command, PL_resupply, resupply, PL_mapStarted, planning, PL_planning])

    #select 4 nodes
    runSequence([PL_map1, node1, PL_n1, node2, PL_n2, node3, PL_n3, node4, PL_n4])

    #execute
    runSequence([PL_n4, execute, PL_executed])

    #wait loop
    for i in range(3):
        singularFight(i)
    cd.runsDone = round(cd.runsDone)

    #end turn
    runSequence([PL_ended, endRound, PL_result])

    #click through, exit to main menu if at end of script
    if cd.runsDone < cd.runsLimit:
        rpt = randPoint(*clickAway)
        while not checkPixels(PL_loading):
            rClick(rpt, (40, 40), 40)
            wait(0.18, 0.03)
    else:
        while not checkPixels(PL_loading):
            rClick(*clickToMainMenu)
            wait(0.18, 0.03)

def singularFight(index):
    while not checkPixels(PL_battle):
        wait(0.04, 0)
    micro(index)
    while checkPixels(PL_battle):
        wait(0.04, 0)
    cd.runsDone += float(1)/float(3)
    wait(2.5, 0.2)
    rpt = randPoint(*clickAway)
    while not checkPixels(PL_loading):
        rClick(rpt, (40, 40), 40)
        wait(0.18, 0.03)

def micro(index):
    if index == 0:
        wait(3.2, 0.05)
        if checkPixels(PL_battle):
            positionSelected(*posGrid[5])
            wait(0.1, 0.05)
        if checkPixels(PL_battle):
            withdraw()
            wait(0.1, 0.05)
    elif index == 2:
        wait(4.7666, 0.05)
        if checkPixels(PL_battle):
            positionSelected(*posGrid[5])
            wait(0.1, 0.05)
        if checkPixels(PL_battle):
            withdraw()
            wait(0.1, 0.05)
        if checkPixels(PL_battle):
            wait(1.7, 0.04)
        if checkPixels(PL_battle):
            positionSelected(*posGrid[4])
            wait(0.1, 0.05)
        if checkPixels(PL_battle):
            withdraw()
            wait(0.1, 0.05)

def testRun():
    #param = ((1248, 735), (104.5, 36.0), 0)
    for _ in range(10):
        #rClick(*param)
        rDrag(*(randPoint((1142, 202), (200, 120)), randPoint((1202, 797), (250, 100)), 150, 0.2))
