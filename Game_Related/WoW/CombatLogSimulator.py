# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random


wpnMinDmg = 50
wpnMaxDmg = 100
wpnSpeed = 4
attackPower = 500
apDPS = attackPower/14
hit = 0.9
crit = 0.15
socPPH = wpnSpeed/(60/7)
attackCooldown = wpnSpeed
enemyArmour = 0.4


def SoC():
    socRoll = random.random()
    if socRoll < crit:
        dmg = dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1.4)
        print("You SoC hits your foe for {} holy damage(CRIT!).".format(int(round(dmg))))
    elif socRoll < hit:
        dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(0.7)
        print("Your SoC hits your foe for {} holy damage.".format(int(round(dmg))))
    else:
        print("Your SoC missed!")


def attack():
    attackRoll = random.random()
    socRoll = random.random()
    if attackRoll < crit:
        dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1-enemyArmour)*2
        print("You attack your foe for {} physical damage(CRIT!)".format(int(round(dmg))))
        if socRoll < socPPH:
            SoC()
    elif attackRoll < hit:
        dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1-enemyArmour)
        print("You attack your foe for {} damage.".format(int(round(dmg))))
        if socRoll < socPPH:
            SoC()
    else:
        print("You miss!")


for t in range(10000):
    attackCooldown -= 0.1
    if attackCooldown <= 0:
        attack()
        attackCooldown = wpnSpeed
