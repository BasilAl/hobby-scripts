import random

def rand(a, b, d=1,p=0):
    s = 0
    for i in range(d):
        s += random.randint(a, b)
    return s+p

dices = [4,6,8,10,12]
NUMBER=100000
print("""Calculates the effect of changing the D&D crit rule from rolling
the dice twice to rolling the dice and adding the max possible to the result
for different levels of bonus dmg(from attributes,enchants etc)""")
for plus in range(2,13):
    print()
    print("For +{} bonus to damage:".format(plus))
    for side in dices:
        basicS=0
        altS=0
        for i in range(NUMBER):
            a=rand(1,side,p=plus)
            basicS+=a
            altS+=a
            altS+=side
            basicS+=rand(1,side)
        basicS=basicS/NUMBER
        altS=altS/NUMBER
        print("D{}: Basic Crit: {:.3f} Alt Crit: {:.3f} +increase: {:.3f} %increase: {:.3f}".format(side,basicS,altS,altS-basicS,100*(altS/basicS-1)))
