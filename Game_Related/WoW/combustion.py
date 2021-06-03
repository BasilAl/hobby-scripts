# Combustion Calculator
import random
# BaseCrit = 0.5
# Crit = BaseCrit


def Fireball():
    global Crit
    global critcount
    global hitcount
    global misscount
    global Fcast
    global CmbCount
    if Fcast <= 0:
        castroll = random.random()
        Fcast = 2.9
        if castroll < Crit:
            critcount += 1
            CmbCount += 1
        elif castroll < 0.99:
            hitcount += 1
        else:
            misscount += 1
    else:
        Fcast -= 0.1


for i in range(0, 60, 5):
    BaseCrit = i/100
    Crit = BaseCrit

    hits = 0
    crits = 0
    CmbCD = 0
    Fcast = 3
    CmbCount = 5
    hitcount = 0
    critcount = 0
    misscount = 0
    CMBused = 0

    for t in range(1800003):
        if CmbCD <= 0:
            CMBused += 1
            CmbCount = 0
            CmbCD = 180
        if CmbCount >= 3:
            Crit = BaseCrit
            Fireball()
        else:
            Crit += 0.1
            Fireball()
        CmbCD -= 0.1

    total = hitcount+critcount+misscount
    print("=================================")
    #print("Total Count:  {}".format(total))
    #print("Crit Count:   {}".format(critcount))
    #print("Hit  Count:   {}".format(hitcount))
    #print("Miss Count:   {}".format(misscount))
    #print("Combustions:   {}".format(CMBused))
    print("Base Crit:    {}".format(BaseCrit))
    print("Crit Chance:  {}%".format((critcount/(hitcount+critcount)*100)))
    print("Crit Gained:  {}%".format((critcount/(hitcount+critcount)-BaseCrit)*100))
    print("=================================")
