# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random


'''
21 Agi: 1 Crit
+.015 crit/-dodge from skill
Paladin Base Stats:
Str/Agi/Sta/Int/Spi
Base Mana:1232
Base Health:1201
Base AP: 160
Bonuses:83/45/78/50/54
Human: 22 /20 /22 /20 /21
Human total:
        Str:105
        Agi:65
        Sta:100
        Int:70
        Spi:82
        AP:370
        Armor: 130(2*Agi)
'''

'''Gear Bonuses:
Cloak: Zulian Tigerhide Cloak: 13 agi, 10 sta 1 hit
Neck:Blazefury Medallion: 13 Agi, 14 Sta, 2+.5*SP dmg on hit
Rings1:Don Julio's: 11 Sta, 1 hit, 1 crit, 16 AP
Ring2:Band of Jin: 14 Agi, 8 Sta, 1 hit
Trinkets: Briarwood Reed(29 SP), HoJ(2% extra swing, 20 AP)
Judgment Full set:
Str:92
Agi:0
Sta:155
Int:148
Spi:50
SP:153+47=200
MP5:20

Enchants:
4 stats(chest)
Weapon: 30 SP
Head/Legs: 8SP
Gloves/Boots 7 Agi
Bracers: 5MP5

Total Stats:
Health:4221
Mana:4562
Str:301
Agi:123
Sta:302
Int:222
Spi:136
AP:160+594+36=790
SP:245
Hit:3+3(tal)=6
Crit:1+5(tal)+5(base)+5.85(Agi)=16.85
MP5:25



'''

proc = {
    "health": 4221,
    "mana": 4562,
    "str": 301,
    "agi": 123,
    "sta": 302,
    "int": 222,
    "spi": 136,
    "AP": 790,
    "SP": 245,
    "hit": 0.03,
    "crit": 0.168,
    "mp5": 25
}

retri = {
    "health": 4221,
    "mana": 2702,
    "str": 280,
    "agi": 304,
    "sta": 302,
    "int": 98,
    "spi": 82,
    "AP": 910,
    "SP": 0,
    "hit": 0.07,
    "crit": 0.325,
    "mp5": 0
}
wpnSpeed = 3.5
AP = 979
apDPS = AP/14
wpnMinDmg = 229+(AP/14)*wpnSpeed
wpnMaxDmg = 344+(AP/14)*wpnSpeed
hit = 7
crit = 0.15
socPPH = wpnSpeed/(60/7)
attackCooldown = wpnSpeed
enemyArmour = 0.4

target_dmg = 0


def PPM(ppm, Speed):
    return (ppm*speed)/60


def onHit():
    # Drake Talon CLeaver
    if random.random() <= 0.6:
        target_dmg += 240/enemyArmour
        print("Drake Talon Cleaver Proc: {} dmg".format(enemyArmour))
        onHit()
    # Kazzak Neck
    neck_dmg = 2+SP*0.5
    target_dmg += neck_dmg
    print("Kazzak Neck proc: {}", neck_dmg)
    # Maelstrom Trinket
    '''
    Not enough info on coefficient
    if random.random()<=PPM(1,3.4):
        target_dmg+=random.randint(201,300)
        '''
    # HoJ
    if random.random() <= 0.02:
        attack()
    # SoR
    '''Leei 21-72+12.5%SP alla an thymamai kala scalarei me to weapon speed
    kai to coefficient
    TESTED THOROUGHLY: (23+.11*SP)*wpnspeed'''
    sor = (23+0.11*SP)*wpnSpeed
    print("Target takes {} SoR dmg".format(sor))

    # Oil
    if random.random() <= 0.15:
        '''Casts Shadowbolt Rank 3 15% chance:
        Coefficient should be:
        1: cast time(2.8)=>0.8
        2: number of targets its designed for(1)
        3: additional effects(1)
        4: the level you first get the spell(Level * 3/20 + 1) / 4
        4: lvl 12: 0.55
        total = .55*.8=.44'''
        oil_dmg = random.randint(49, 58) + SP*.44
        target_dmg += oil_dmg
        print("Shadow Oil dmg: {}".format(oil_dmg))


def SoC():
    '''SoC dmg is 70% weapon +30% SP'''
    socRoll = random.random()
    if socRoll < crit:
        dmg = dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(1.4)
        print("You SoC hits your foe for {} holy damage(CRIT!).".format(int(round(dmg))))
    elif socRoll < hit:
        dmg = random.randint(wpnMinDmg, wpnMaxDmg)*(0.7)
        print("Your SoC hits your foe for {} holy damage.".format(int(round(dmg))))
    else:
        print("Your SoC missed!")


def attackRoll():
    '''Attack Table:
    -Critical Strike chance is reduced by 1% per each additional level the target
     has over the player. (So if you have a 4% chance to crit an at-level target,
     you have a 1% chance to crit a +3-level target, in both clients.)

    -There is some code in 1.12 that explicitly adds a modifier that causes the
    first 1% of +hit gained from talents or gear to be ignored against monsters
    with more than 10 Defense Skill above the attacking player’s Weapon Skill.
    This means that the so-called “hit cap” is in effect 9% rather than 8% for a
    player with 300 Weapon Skill fighting a level 63 monster with a Defense Skill of 315.

    -’m not going to get too deep into the specific math on this one, but for the
    sake of clarity, I’ll say that this is not a per-aura modifier and it is separate
    than the 3% suppression that is baseline against +3 level creatures.
    There is a single modifier placed on total Critical Strike gained from auras
    that increase Crit chance such as those I listed in my last post.

    1)Miss(5%+(Def-Skill)*.1% if def-skill<=10 or 6%+(def-skill-10)*.4%)
    2)Dodge(5%)
    3)Parry(5%(0 if positioned))
    4)Glancing Blow(40% for .75(+weapon skill) dmg)
    5)Block(0 if positioned)
    6)Crit
    7)Hit'''
    aR = random.random()
    if aR <= 0.05:
        print("MISS")
    elif aR < 0.1:
        print("DODGE")
    elif aR < 0.5:
        # Glancing!
        pass
    elif aR < 0.5+crit:
        # CRIT!
        pass
    else:
        # Hit
        pass


for t in range(10000):
    attackCooldown -= 0.1
    if attackCooldown <= 0:
        attackRoll()
        attackCooldown = wpnSpeed
