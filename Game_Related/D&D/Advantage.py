import random


def roll(d=10, gwf=0):
    result = random.randint(1, d)
    if (result < 3 and gwf == 1):
        result = random.randint(1, d)
    return result


iterations = 1000000
sum = 0
adv = 0
dis = 0
print('====== Roll 20 Averages ======')

for i in range(iterations):
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    high = max(roll1, roll2)
    low = min(roll1, roll2)
    sum += roll1
    adv += high
    dis += low

print("Normal average:        {}".format(sum/iterations))
print("Advantage average:     {}".format(adv/iterations))
print("Disadvantage average:  {}".format(dis/iterations))
print("Advantage Bonus:      +{}".format((adv-sum)/iterations))
print("Disadvantage Bonus:   -{}".format((sum-dis)/iterations))


'''
sum1 = 0
sum2 = 0
iterations = 1000000
for i in range(iterations):
    sum1 += roll(10, 0)
    sum2 += roll(10, 1)
avg1 = sum1/iterations
avg2 = sum2/iterations

print("Without GWF: {}".format(avg1))
print("With GWF   : {}".format(avg2))
print("Difference : {}".format(avg2-avg1))
'''
