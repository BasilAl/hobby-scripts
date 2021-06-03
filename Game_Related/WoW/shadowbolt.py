import random
import numpy

# 455-507

def Shadowbolt(sp=800, crit=28, hit=11, improved=1):
    global ImprovedCount
    hitchance = min(99, 83+hit)
    castroll = random.random()
    imptemp = 0
    if castroll < hitchance/100:
        critroll = random.random()
        if critroll < crit/100:
            dmg = 2*(random.randint(455, 508)+3*sp/3.5)
            if improved == 1:
                imptemp = 1
        else:
            dmg = (random.randint(455, 508)+3*sp/3.5)
    else:
        dmg = 0
    if ImprovedCount > 0:
        dmg = dmg*1.2
        ImprovedCount -= 1
    if imptemp > 0:
        ImprovedCount = 2
    return dmg


ImprovedCount = 0
iterations = 15
global TotalDmg
TotalDmg = 0
global AverageList
AverageList = []
for i in range(50):
    TotalDmg = 0
    for i in range(iterations):
        ImprovedCount = 0
        tempdmg = Shadowbolt()
        TotalDmg += tempdmg
    avg1 = TotalDmg/iterations

    ImprovedCount = 0
    TotalDmg = 0
    for i in range(iterations):
        ImprovedCount = 0
        tempdmg = Shadowbolt(800, 23, 16, 1)
        TotalDmg += tempdmg
    avg2 = TotalDmg/iterations
    AverageList.append((avg2-avg1, avg2, avg1))
#print("Hit : 0, average dmg: {}".format(avg1))
#print("Hit : 1, average dmg: {}".format(avg2))
averages = []
for line in AverageList:
    # print(line)
    averages.append(line[0])

print("Average gain from hit: {}".format(numpy.average(averages)))
print("Number of fights: "+str(len(AverageList)))
better = 0
for i in range(len(AverageList)):
    if AverageList[i][0] >= 0:
        better += 1

print("Hit is better on "+str(better)+" fights.")
print("Crit is better on "+str(len(AverageList)-better)+" fights")
