import random
import math

"""Dice roller generates average values and samples for the following rolls :
3d6, 4d6dl1, 3d6r1, 4d6r1dl1 kai 4d6dl1r1 (dl1=drop lowest 1, r1=reroll 1s)
"""


def r3d6():
    s = 0
    for i in range(3):
        s += random.randint(1, 6)
    return s


def r3d6r1():
    s = 0
    for i in range(3):
        s += random.randint(2, 6)
    return s


def r4d6dl():
    a = []
    for i in range(4):
        a.append(random.randint(1, 6))
    a.sort()
    s = 0
    for i in range(len(a) - 1):
        s += a[i + 1]
    return s


def r4d6r1dl():
    a = []
    for i in range(4):
        a.append(random.randint(2, 6))
    a.sort()
    s = 0
    for i in range(len(a) - 1):
        s += a[i + 1]
    return s


def r4d6dlr1():
    a = []
    for i in range(4):
        a.append(random.randint(1, 6))
    a.sort()
    b = []
    for i in range(len(a) - 1):
        b.append(a[i + 1])
    for i in range(3):
        if b[i] == 1:
            b[i] = random.randint(2, 6)
    s = 0
    for i in range(3):
        s += b[i]
    return s


def attributes(dicef):
    a = []
    for i in range(6):
        a.append(dicef())
    return a


def stats(dicef):
    temp = []
    tm = 0
    tv = 0
    for i in range(100000):
        tem = dicef()
        tm += tem
        temp.append(tem)
    M = tm / 100000
    for i in range(100000):
        tv += (temp[i] - M) ** 2
    VAR = tv / 100000
    return (M, VAR)


if __name__ == "__main__":
    print("Roll   : Average  , Variance ")
    print("=====================================")
    print("3d6    : " + str(stats(r3d6)))
    print("3d6r1  : " + str(stats(r3d6r1)))
    print("4d6dl  : " + str(stats(r4d6dl)))
    print("4d6r1dl: " + str(stats(r4d6r1dl)))
    print("4d6dlr1: " + str(stats(r4d6dlr1)))
    print("\n\n\n\n")
    print("Roll   :  Sample Pool ")
    print("=================================")
    print("3d6    : " + str(attributes(r3d6)))
    print("3d6r1  : " + str(attributes(r3d6r1)))
    print("4d6dl  : " + str(attributes(r4d6dl)))
    print("4d6r1dl: " + str(attributes(r4d6r1dl)))
    print("4d6dlr1: " + str(attributes(r4d6dlr1)))

# input("press any key to continue...")
