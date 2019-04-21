from utilDriver import *
from utilPrimitive import *
from utilContext import *

# Don't mind me, I'm just stealing a bunch of data points for things
PL_dollSelect = [((293, 52), (255, 255, 255)), ((1569, 170), (49, 48, 49)), ((1554, 183), (255, 255, 255)), ((1569, 298), (49, 48, 49)), ((1551, 313), (255, 255, 255)), ((1213, 457), (239, 239, 239))]
filterBy = (((1510, 329), (89.0, 55.5), 0), 0.5, 0.3, False)
PL_filter = [((1138, 746), (255, 162, 0)), ((1071, 743), (255, 255, 255)), ((943, 521), (255, 255, 255)), ((1289, 464), (255, 255, 255))]
mgSelect = (((1103, 538), (78.0, 29.5), 0), 0.5, 0.3, False)
PL_mgOnly = [((1127, 521), (255, 180, 0)), ((1445, 345), (255, 180, 0)), ((344, 44), (255, 255, 255))]
confirmFilter = (((1250, 745), (124.0, 20.0), 0), 1.3, 0.3, False)
PL_filtered = [((1441, 353), (255, 182, 0)), ((1570, 297), (49, 48, 49)), ((1549, 312), (255, 255, 255)), ((290, 54), (255, 255, 255)), ((1213, 456), (239, 239, 239))]

# From main screen
factory = (((1470, 453), (101.0, 35.5), 0), 2, 1, False)
cancel = (((341, 80), (58.5, 38.0), 0), 1, 1, False)
PL_intro_factory = [((283, 44), (255, 187, 0)), ((347, 181), (255, 180, 0)), ((352, 386), (247, 247, 247)), ((348, 512), (214, 214, 214))]

PL_doll_star = [((445, 159), (255, 186, 0))]
PL_doll_star_special = [((427, 349), (206, 85, 206))]

PL_doll_star_selected = [((445, 159), (255, 239, 189))]
PL_doll_star_selected_special = [((353, 153), (247, 239, 255)), ((427, 349), (206, 85, 206))]

# Factory base - left-hand sidebar for "t-doll enhancement"
enhance_factory = (((362, 391), (88.5, 40.0), 0), 1, 0.5, False)
enhance_target_select = (((601, 477), (81.5, 146.5), 0), 1, 0.5, False)
enhance_target_selectDoll = (((370, 298), (69.5, 135.0), 0), 1, 0.5, False)
enhance_fodder_select = (((827, 250), (79.5, 42.5), 0), 1, 0.5, False)
enhance_fodder_smartSel = (((1511, 687), (74.0, 42.0), 0), 1, 0.5, False)
enhance_fodder_smartSel_cond = ((1511, 687), (74.0, 42.0), 0)
enhance = (((1506, 935), (76.0, 23.0), 0), 1, 0.5, False)
enhance_target_select2 = ((605, 825), (88.0, 20.5), 0)
PL_enhancement = [((342, 45), (255, 186, 0)), ((316, 365), (140, 97, 0)), ((340, 364), (255, 182, 0)), ((1362, 872), (41, 203, 181)), ((1548, 873), (41, 203, 181))]
PL_enhancement_target_select = [((338, 107), (255, 255, 255)), ((1569, 170), (49, 48, 49)), ((1551, 184), (255, 255, 255)), ((1570, 298), (49, 48, 49)), ((1552, 314), (255, 255, 255))]
PL_enhancement_target_set = [((1363, 874), (41, 203, 181)), ((1547, 873), (41, 203, 181)), ((1515, 921), (255, 223, 0)), ((1271, 921), (49, 48, 49))]
PL_enhancement_fodder = [((339, 107), (255, 255, 255)), ((1508, 653), (33, 32, 33)), ((1569, 300), (49, 48, 49)), ((1551, 311), (255, 255, 255)), ((1570, 170), (49, 48, 49)), ((1551, 180), (255, 255, 255))]
PL_enhancement_fodder_selected = [((1507, 654), (255, 186, 0)), ((1476, 698), (49, 48, 49))]
PL_enhanced = [((907, 704), (49, 48, 49)), ((890, 691), (49, 48, 49)), ((889, 678), (255, 255, 255)), ((921, 716), (239, 239, 239))]

# Enhancement targets
tdoll_target_to_enhance = (((603, 569), (91.0, 276.0), 0), 0.5, 0.4, False)
select_fodder_enhance = (((826, 250), (90.0, 53.5), 0), 0.5, 0.4, False)

# Factory base - left-hand sidebar for "retirement disassemble"
retirement_factory = (((363, 489), (89.0, 40.0), 0), 1, 0.5, False)
PL_retirement = [((350, 507), (219, 155, 0)), ((576, 211), (253, 176, 0)), ((792, 212), (254, 178, 0)), ((1486, 967), (255, 187, 0))]

# Retirement targets
select_fodder_retire_tdoll = (((635, 235), (75.5, 40.5), 0), 1, 1, False)
PL_retire_tdoll_readyselect = [((1433, 419), (255, 255, 255)), ((333, 52), (255, 255, 255)), ((1442, 670), (34, 34, 34))]
PL_retire_tdoll_postselect = [((1540, 671), (255, 187, 0)), ((1444, 456), (51, 51, 51)), ((334, 52), (255, 255, 255)), ((1536, 167), (255, 255, 255))]

# Also serves as the "ok"
smart_select = (((1505, 704), (74.5, 44.0), 0), 1, 0.75, False)
smart_select_cond = ((1505, 704), (74.5, 44.0), 0)

# burn the fodder
manage_confirm = (((1494, 941), (72.0, 23.5), 0), 0.5, 0.4, False)
PL_fodder_selected = [((284, 41), (255, 187, 0)), ((1506, 963), (255, 187, 0)), ((1253, 957), (51, 51, 51))]

# gtfo my face
back_to_base = (((344, 77), (58.0, 37.0), 0), 0.5, 0.4, False)

# repair
repair = (((1238, 506), (100.0, 29.0), 0), 1, 1, False)
repair_select = ((413, 497), (77.0, 151.5), 0)
repair_select_doll = (((368, 293), (72.5, 134.5), 0), 1, 1, False)
repair_ok = (((1510, 610), (75.0, 44.0), 0), 1, 1, False)
repair_quick = (((601, 693), (31.5, 30.5), 0), 1, 1, False)
repair_confirm = (((1239, 690), (76.5, 21.5), 0), 1.5, 1.5, False)
repair_done = (((939, 705), (78.5, 25.0), 0), 1.5, 1.5, False)
repair_toBase = ((341, 78), (61.0, 37.5), 0)
PL_repair = [((340, 47), (255, 186, 0)), ((503, 60), (255, 255, 255)), ((479, 94), (255, 255, 255)), ((467, 82), (16, 20, 16))]
PL_repair_select = [((340, 54), (255, 255, 255)), ((1546, 579), (247, 182, 0)), ((1475, 623), (49, 48, 49)), ((1570, 167), (49, 48, 49)), ((1551, 184), (255, 255, 255))]
PL_repair_confirm = [((1219, 705), (255, 186, 0)), ((1199, 705), (49, 48, 49)), ((628, 719), (255, 255, 255)), ((601, 706), (49, 48, 49))]
PL_repair_confirm_quick = [((602, 721), (255, 186, 0)), ((612, 706), (49, 48, 49))]
PL_repair_done = [((685, 414), (255, 255, 255)), ((891, 717), (49, 48, 49)), ((972, 684), (255, 255, 255)), ((686, 440), (255, 185, 0))]

# Reference points to get back from "Combat" screen
PL_ET_phone_home = [((307, 45), (255, 187, 0)), ((376, 213), (210, 148, 0)), ((509, 626), (255, 180, 0)), ((1422, 148), (255, 180, 0))]
PL_mainMenu = [((278, 538), (255, 182, 0)), ((277, 148), (57, 195, 255)), ((1582, 1014), (255, 255, 255)), ((1583, 60), (255, 182, 0))]

# Not used yet; will be used when enhancement is implemented
def filterMG():
    runSequence([PL_filter, mgSelect, PL_mgOnly, confirmFilter, PL_filtered])

# disassembly script; run this to burn your 2-star undesirables!!!!
def burn_fodder(runManagement = True):
    #cd.DEBUG_RUNNING = True
    # Logistic sync happens right before this
    #   -For now assume that the setting left enough time for Enhancements, Fodder dump, Repair (line up logis and do 1 hours segments)
    #       -For the sake of simplicity just ignore dumping MG specifically
    #       -Determine if anyone is needed for enhance, enhance them using smart select until no one is left
    #       -Smart select all 2* and dump, for now just save the rarer dolls and sort at the end (just make sure doll cap is far higher)
    #       -Go out to mainscreen and go into repair, determine which boxes are filled and repair all with quick contract, confirm popup
    #       -Go back out to main screen and prepare to restart (waiting for the logistics to restart or just go if everything is above 1 hr)
    #       -Increments a wait value for util logi to kill off and wait on the value
    #   -After doing all the management determine how many logistics restarts are needed within the next short interval (all logis with just minutes left)
    #   -Wait for the restarts in a similar way to checking in map progress and kick off the script as soon as the final logistic is restarted

    if runManagement:
        # Go to factory
        runSequence([PL_mainMenu, factory, PL_intro_factory])

        # probably do some handling for when dump and enhance don't have 2*s to fodder
        doEnhance()
        doDump()
        doRepair()

    doLogistics()
    #cd.DEBUG_RUNNING = False

def doEnhance():
    # initially enter the doll enhancement target selection screen
    runSequence([PL_intro_factory, enhance_factory, PL_enhancement, enhance_target_select, PL_enhancement_target_select])

    # while a star is still detected in the first position (still dolls left to enhance)
    while checkPixels(PL_doll_star) or checkPixels(PL_doll_star_special):
        # set the enhancement target
        runSequence([PL_enhancement_target_select, enhance_target_selectDoll, PL_enhancement_target_set])

        # smart select fodder
        runSequence([PL_enhancement_target_set, enhance_fodder_select, PL_enhancement_fodder])

        rClick(*enhance_fodder_smartSel_cond)
        wait(1)
        if checkPixels(PL_enhancement_fodder_selected):
            runSequence([PL_enhancement_fodder_selected, enhance_fodder_smartSel, PL_enhancement_target_set])
        else:
            runSequence([PL_enhancement_fodder, cancel, PL_enhancement])
            return
        
        # execute enhance, and click on bottom of doll until returned to enhancement target selection
        runSequence([PL_enhancement_target_set, enhance, PL_enhanced])
        while not checkPixels(PL_enhancement_target_select):
            rClick(*enhance_target_select2)
            wait(1)
    
    # Once out of dolls cancel out and get ready to burn
    runSequence([PL_enhancement_target_select, cancel, PL_enhancement])

def doDump():
    # Check if entering from intro_factory
    if checkPixels(PL_intro_factory):
        runSequence([PL_intro_factory, retirement_factory, PL_retirement])
    else:
        # enter from enhancement
        runSequence([PL_enhancement, retirement_factory, PL_retirement])

    # select the plus sign.... smart select the undesirables....
    runSequence([PL_retirement, select_fodder_retire_tdoll, PL_retire_tdoll_readyselect])

    rClick(*smart_select_cond)
    wait(1)
    if checkPixels(PL_retire_tdoll_readyselect):
        runSequence([PL_retire_tdoll_readyselect, cancel, PL_retirement, back_to_base, PL_mainMenu])
        return
    
    # Begin the destruction!!!
    runSequence([PL_retire_tdoll_postselect, smart_select, PL_fodder_selected])
    
    # FINISH THE BURNING!!!!!!!!!!!!.... then go home
    runSequence([PL_fodder_selected, manage_confirm, PL_retirement, back_to_base, PL_mainMenu])

def doRepair():
    if cd.repairSkip < cd.repairSkipLimit:
        cd.repairSkip += 1
        return
    cd.repairSkip = 0

    runSequence([PL_mainMenu, repair, PL_repair])
    injured = True
    while injured:
        while checkPixels(PL_repair):
            rClick(*repair_select)
            wait(0.8)
        # Check if there are dolls to repair
        if checkPixels(PL_repair_select):
            # check if the special sequence is needed
            # this could cause it to get stuck looking for special if the normal star appearance is delayed (could use a longer delay or for now just do a setting)
            if cd.special_repair and not checkPixels(PL_doll_star):
                # the doll to be repaired is special
                runSequence([PL_repair_select, repair_select_doll, PL_doll_star_selected_special, repair_ok, PL_repair_confirm, repair_quick, PL_repair_confirm_quick, repair_confirm, PL_repair_done, repair_done, PL_repair])
            else:
                # run normal sequence
                runSequence([PL_repair_select, repair_select_doll, PL_doll_star_selected, repair_ok, PL_repair_confirm, repair_quick, PL_repair_confirm_quick, repair_confirm, PL_repair_done, repair_done, PL_repair])
        else:
            injured = False
    rClick(*repair_toBase)
    wait(0.8)
    while not checkPixels(PL_mainMenu):
        rClick(*repair_toBase)
        wait(5)

def doLogistics():
    logiSync()
    if cd.logiWait == 0:
        for ct in cd.logiCountdown:
            if not ct == None:
                #if round(ct - time.time()) < 1200:
                if round(ct - time.time()) < 1440:
                #if round(ct - time.time()) < 60:
                    cd.logiWait += 1
        wait(1)
    while cd.logiWait > 0:
        wait(1)
