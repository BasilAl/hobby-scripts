import random


# AC: 10-25 +Hit: +5(+3 str) | +10 (+5 str)

def rand(a, b, d=1,p=0):
    s = 0
    for i in range(d):
        s += random.randint(a, b)
    return s+p




flmtng = []
plustwo = []
STR = 3
HIT = 5
RESULT = []


def attackP2(roll, str, hit, AC):
    # roll=random.randint(1,20)
    if roll == 1:
        return 0
    if roll == 20:
        return rand(1, 8, 2)+str+2
    if (roll+hit+2) >= AC:
        return rand(1, 8)+str+2
    else:
        return 0


def attackFl(roll, str, hit, AC):
    # roll=random.randint(1,20)
    if roll == 1:
        return 0
    if roll == 20:
        return rand(1, 8, 2)+str+rand(1, 6, 4)
    if (roll+hit) >= AC:
        return rand(1, 8)+str+rand(1, 6, 2)
    else:
        return 0


for AC in range(10, 26):
    sfl = 0
    sp2 = 0
    for i in range(10000):
        roll = rand(1, 20)
        sfl += attackFl(roll, STR, HIT, AC)
        sp2 += attackP2(roll, STR, HIT, AC)
    avfl = sfl/10000
    avp2 = sp2/10000
    flmtng.append(avfl)
    plustwo.append(avp2)

#print("STR: 3, PROF=2:")
RESULT.append("STR: 3, PROF=2:")
for i in range(len(flmtng)):
    if flmtng[i] >= plustwo[i]:
        sign = "+"
        prc = (flmtng[i]/plustwo[i]-1)*100
    else:
        sign = "-"
        prc = (1-flmtng[i]/plustwo[i])*100
    RESULT.append("AC: {}: Flametongue: {:.3f} Plus2: {:.3f} difference {}{:.3f}%".format(
        10+i, flmtng[i], plustwo[i], sign, prc))
    # print("AC: {}: Flametongue: {:.3f} Plus2: {:.3f} difference {}{:.3f}%".format(
    #    10+i, flmtng[i], plustwo[i], sign, prc))
    # print("")

# print("")
# print("")
STR = 5
HIT = 10
flmtng = []
plustwo = []
for AC in range(10, 26):
    sfl = 0
    sp2 = 0
    for i in range(10000):
        roll = rand(1, 20)
        sfl += attackFl(roll, STR, HIT, AC)
        sp2 += attackP2(roll, STR, HIT, AC)
    avfl = sfl/10000
    avp2 = sp2/10000
    flmtng.append(avfl)
    plustwo.append(avp2)

#print("STR: 5, PROF=5:")
RESULT.append("STR: 5, PROF=5:")
for i in range(len(flmtng)):
    if flmtng[i] >= plustwo[i]:
        sign = "+"
        prc = (flmtng[i]/plustwo[i]-1)*100
    else:
        sign = "-"
        prc = (1-flmtng[i]/plustwo[i])*100
    RESULT.append("AC: {}: Flametongue: {:.3f} Plus2: {:.3f} difference {}{:.3f}%".format(
        10+i, flmtng[i], plustwo[i], sign, prc))
    # print("AC: {}: Flametongue: {:.3f} Plus2: {:.3f} difference {}{:.3f}%".format(
    #    10+i, flmtng[i], plustwo[i], sign, prc))
    # print("")


for item in RESULT:
    print(item)
