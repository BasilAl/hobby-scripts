# -*- coding: utf-8 -*-
import random
import time
# 110  -
wpnMinDmg = 430
wpnMaxDmg = 580
basewpnSpeed = 3.4  # so that I can implement speed increase
wpnSpeed = 3.5
#attackPower = 500
#apDPS = attackPower/14
hit = 1.0  # capped
crit = 0.215
scrit = 0.05
socPPH = basewpnSpeed/(60/7)
crusaderPPH = basewpnSpeed/60  # /1
attackCooldown = wpnSpeed  # aa cd
enemyArmour = 0.3  # average boss dmg reduction 42-48
SP = 0+30
CRUSADER = 1  # checks if enchant is active
SULFURAS = 0
joccd = 0  # judment of command cooldown

# Initialisation of variables(some are reinitialized later, doesn't matter)
attackCooldown = 0
vengeancedur = 0
totaldmg = 0
sulfurasdmg = 0
swingdmg = 0
jocdmg = 0
socdmg = 0
joccounter = 0
soccounter = 0
swingcounter = 0
crusaderdur = 0


def SoC():
    global socdmg
    global totaldmg
    socRoll = random.random()
    if socRoll < crit:
        # nightfall()
        if SULFURAS == 1:
            sulfuras()
        if crusaderdur > 0:
            dmg = dmg = random.randint(wpnMinDmg+int(14.29*wpnSpeed),
                                       wpnMaxDmg+int(14.29*wpnSpeed))*(1.4) + 0.6*SP
        else:
            dmg = dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1.4) + 0.6*SP
        if vengeancedur >= 0:
            dmg *= 1.15
        Vengeance()
        if(CRUSADER == 1):
            crusader()
        #print("You SoC hits your foe for {} holy damage(CRIT!).".format(int(round(dmg))))
        HoJ()
    elif socRoll < hit:
        # nightfall()
        if SULFURAS == 1:
            sulfuras()
        if crusaderdur > 0:
            dmg = random.randint(wpnMinDmg+int(14.29*wpnSpeed), wpnMaxDmg +
                                 int(14.29*wpnSpeed))*(0.7)+0.3*SP
        else:
            dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(0.7)+0.3*SP
        if vengeancedur >= 0:
            dmg *= 1.15
        if(CRUSADER == 1):
            crusader()
        #print("Your SoC hits your foe for {} holy damage.".format(int(round(dmg))))
        HoJ()
    else:
        #print("Your SoC missed!")
        dmg = 0
    totaldmg += dmg
    socdmg += dmg


def sulfuras():
    global totaldmg
    global sulfurasdmg
    sulfroll = random.random()
    if sulfroll <= 0.1:
        totaldmg += 375
        sulfurasdmg += 375
        if random.random() <= scrit:
            totaldmg += 150
            sulfurasdmg += 150


def attack():
    global totaldmg
    global swingdmg
    global soccounter
    global swingcounter
    attackRoll = random.random()
    socRoll = random.random()
    if attackRoll < 1-hit:
        # print("MISS")
        dmg = 0
    elif attackRoll < (1-hit)+0.05:
        # print("Dodge")
        dmg = 0
    elif attackRoll < 1-hit+0.35:
        nightfall()
        nightfall()
        if SULFURAS == 1:
            sulfuras()
        swingcounter += 1
        if crusaderdur > 0:
            dmg = random.randint(wpnMinDmg+int(14.29*wpnSpeed), wpnMaxDmg +
                                 int(14.29*wpnSpeed))*(1-enemyArmour)
        else:
            dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1-enemyArmour)
        if vengeancedur >= 0:
            dmg *= 1.15
        if(CRUSADER == 1):
            crusader()
        dmg *= 0.85
        #print("You attack your foe for {} damage(GLANCING).".format(int(round(dmg))))
        HoJ()
        if socRoll < socPPH:
            SoC()
            soccounter += 1
    elif attackRoll < 1-hit+0.35+crit:
        # glancing
        nightfall()
        nightfall()
        if SULFURAS == 1:
            sulfuras()
        swingcounter += 1
        if crusaderdur > 0:
            dmg = random.randint(wpnMinDmg+int(14.29*wpnSpeed), wpnMaxDmg +
                                 int(14.29*wpnSpeed))*(1-enemyArmour)*2
        else:
            dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1-enemyArmour)*2
        if vengeancedur >= 0:
            dmg *= 1.15
        Vengeance()
        if(CRUSADER == 1):
            crusader()
        #print("You attack your foe for {} physical damage(CRIT!)".format(int(round(dmg))))
        HoJ()
        if socRoll < socPPH:
            SoC()
            soccounter += 1
    else:
        nightfall()
        nightfall()
        if SULFURAS == 1:
            sulfuras()
        swingcounter += 1
        if crusaderdur > 0:
            dmg = random.randint(wpnMinDmg+int(14.29*wpnSpeed), wpnMaxDmg +
                                 int(14.29*wpnSpeed))*(1-enemyArmour)
        else:
            dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1-enemyArmour)
        if vengeancedur >= 0:
            dmg *= 1.15
        if(CRUSADER == 1):
            crusader()
        #print("You attack your foe for {} damage.".format(int(round(dmg))))
        HoJ()
        if socRoll < socPPH:
            SoC()
            soccounter += 1
    totaldmg += dmg
    swingdmg += dmg


def JoC():
    global jocdmg
    global totaldmg
    global wpnMinDmg
    global wpnMaxDmg
    attackRoll = random.random()
    if attackRoll <= crit:
        # nightfall()
        dmg = random.randint(169, 187)*2+0.86*SP
        if vengeancedur >= 0:
            dmg *= 1.15
        Vengeance()
        #print("Your Judgment of Command Crits for {} damage(CRIT!).".format(int(round(dmg))))
    elif attackRoll <= hit:
        # nightfall()
        dmg = random.randint(169, 187)+0.43*SP
        if vengeancedur >= 0:
            dmg *= 1.15
        #print("Your Judgment hit for {} holy damage".format(int(round(dmg))))
    else:
        dmg = 0
        #print("Your JoC missed")

    totaldmg += dmg
    jocdmg += dmg


def Vengeance():
    global vengeancedur
    # print("Vengeance!")
    vengeancedur = 8


def crusader():
    # 1 PPM, 14.29 dps*wpn speed
    # int(14.29*wpnSpeed)
    global crusaderdur
    if random.random() <= crusaderPPH:
        # print("Crusader")
        crusaderdur = 15


def nightfall():
    global nightfalldur
    if random.random() <= 0.12:
        nightfalldur = 5


def HoJ():
    if random.random() <= 0.02:
        #print("HOJ PROC!!")
        attack()


attackcooldown = 0
joccd = 0
vengeancedur = 0
totaldmg = 0
socdmg = 0
jocdmg = 0
joccounter = 0
soccounter = 0
swingcounter = 0
vengeanceuptime = 0
crusaderuptime = 0
crusaderdur = 0
nightfalldur = 0
nightfalluptime = 0

for t in range(180000):  # 30min fight
    # time
    attackCooldown -= 0.1
    joccd -= 0.1
    vengeancedur -= 0.1
    crusaderdur -= 0.1
    nightfalldur -= 0.1
    if nightfalldur >= 0:
        nightfalluptime += 0.1
    if crusaderdur >= 0:
        crusaderuptime += 0.1
    if vengeancedur >= 0:
        vengeanceuptime += 0.1
    if attackCooldown <= 0:
        attack()
        attackCooldown = wpnSpeed
    if joccd <= 0:
        JoC()
        joccounter += 1
        joccd = 8
print('''Dmg done in 300 minutes: {0},
        Average SoC dmg = {1},
        Average Swing Dmg = {2}
        Average JoC dmg = {3}
        Total DPS = {4},
        vengeance uptime= {5}sec({6}%)
        crusader uptime = {7}sec({8}%)
        nightfall uptime = {9}sec({10}%)
        '''.format(int(round(totaldmg)), round(socdmg/soccounter, 2),
                   round((totaldmg-socdmg-jocdmg)/swingcounter, 2), round(jocdmg/joccounter, 2),
                   round(totaldmg/18000, 2), round((vengeanceuptime)/10, 2),
                   round((vengeanceuptime)/180, 2), round((crusaderuptime)/10, 2),
                   round((crusaderuptime)/180, 2), round((nightfalluptime)/10, 2), round((nightfalluptime)/180, 2)))


# 12% nightfall: SoC/JoC: 26-28% uptime
# 12% nightfall: SoR: 27-30% uptime
