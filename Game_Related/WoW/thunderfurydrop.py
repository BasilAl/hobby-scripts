import random

player = {"head": 1, "shoulders": 0, "chest": 0, "wrist": 0,
          "hands": 0, "waist": 0, "legs": 1, "feet": 0}


def checkFull(player):
    for i in player:
        if player[i] == 0:
            return 0
    return 1


def makeTFwielder(amount):
    l = []
    for i in range(amount):
        l.append({"left": 0, "right": 0})
    return l


def makePlayers(amount):
    l = []
    for i in range(amount):
        l.append({"head": 1, "shoulders": 0, "chest": 0, "wrist": 0,
                  "hands": 0, "waist": 0, "legs": 1, "feet": 0})
    return l


def mcRun(players):
    if random.random() <= 0.03:
        drop = "right"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
            random.shuffle(nothave)
            if len(nothave) >= 1:
                players[nothave[0]][drop] = 1
    if random.random() <= 0.03:
        drop = "left"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
            random.shuffle(nothave)
            if len(nothave) >= 1:
                players[nothave[0]][drop] = 1


def bwlRun(players):
    # Razorgore(wrist)
    if random.random() <= 0.125:
        drop = "wrist"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.125:
        drop = "wrist"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    # Vaelstrasz(waist)
    if random.random() <= 0.125:
        drop = "waist"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.125:
        drop = "waist"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    # Broodlord(feet)
    if random.random() <= 0.125:
        drop = "feet"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.125:
        drop = "feet"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    # Chromaggus(shoulders)
    if random.random() <= 0.125:
        drop = "shoulders"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.125:
        drop = "shoulders"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    # nefarian(chest)
    if random.random() <= 0.125:
        drop = "chest"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.125:
        drop = "chest"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    # Drakes(hands)
    if random.random() <= 0.0625:
        drop = "hands"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.0625:
        drop = "hands"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1
    if random.random() <= 0.0625:
        drop = "hands"
    else:
        drop = "none"
    if drop in players[0]:
        nothave = []
        for i in range(len(players)):
            if players[i][drop] == 0:
                nothave.append(i)
        random.shuffle(nothave)
        if len(nothave) >= 1:
            players[nothave[0]][drop] = 1


runsforfull = {"1": (0, 0), "2": (0, 0), "3": (0, 0), "4": (
    0, 0), "5": (0, 0), "6": (0, 0), "7": (0, 0), "8": (0, 0)}

runsfortf = {"1": (0, 0), "2": (0, 0), "3": (0, 0), "4": (
    0, 0)}


def runTF(amount):
    players = makeTFwielder(amount)
    runs = 0
    firstFull = 0
    allFull = 0
    keeprunning = 1
    while keeprunning == 1:
        mcRun(players)
        runs += 1
        keeprunning = 0
        for player in players:
            if ((firstFull == 0) and (checkFull(player))):
                firstFull = runs
            if not checkFull(player):
                keeprunning = 1
    allFull = runs
    return(amount, firstFull, allFull)
    print("For {} player(s): {} for first, {} for all".format(amount, firstFull, allFull))


def runFor(amount):
    players = makePlayers(amount)
    runs = 0
    firstFull = 0
    allFull = 0
    keeprunning = 1
    while keeprunning == 1:
        bwlRun(players)
        runs += 1
        keeprunning = 0
        for player in players:
            if ((firstFull == 0) and (checkFull(player))):
                firstFull = runs
            if not checkFull(player):
                keeprunning = 1
    allFull = runs
    return(amount, firstFull, allFull)
    print("For {} player(s): {} for first, {} for all".format(amount, firstFull, allFull))


for numbers in range(1, 4):
    firstF = []
    allF = []
    for i in range(500):
        temp = runTF(numbers)
        firstF.append(temp[1])
        allF.append(temp[2])
    s = 0
    for i in firstF:
        s += i
    first = s/500
    s = 0
    for i in allF:
        s += i
    all = s/500
    runsfortf[str(numbers)] = (first, all)

for amount in runsfortf:
    print("With {} player(s) it takes {} runs for the first and {} for all to get TF on average.".format(
        amount, runsfortf[amount][0], runsfortf[amount][1]))

'''
for numbers in range(1, 9):
    firstF = []
    allF = []
    for i in range(500):
        temp = runFor(numbers)
        firstF.append(temp[1])
        allF.append(temp[2])
    s = 0
    for i in firstF:
        s += i
    first = s/500
    s = 0
    for i in allF:
        s += i
    all = s/500
    runsforfull[str(numbers)] = (first, all)


for amount in runsforfull:
    print("With {} player(s) it takes {} runs for the first and {} for all to get full T2 on average.".format(
        amount, runsforfull[amount][0], runsforfull[amount][1]))
'''
