import random
import time
#thelw na pernaei xronos ana 0.1 sec.
#kathe fora pou teleiwnei to cd apo to autoattack na rixnei autoattack
#kathe fora pou teleiwnei to cd apo kapoio skill na kanei to skill me ena prio list

AP=1000
ws=3.80
wdmin=320
wdmax=400
cc=0.28
sp=120

#timers
global aat=3.8
def autoattack(t):
    global aat
    crit=False
    if random.random()<cc:
        crit=True
    if crit==True:
        damage=2*(random.random(wdmin,wdmax)+AP/14*ws)
    else:
        damage=(random.random(wdmin,wdmax)+AP/14*ws)
    aat=3.8
    if crit==True:
        print(int(t/600),':',t/10%60,'You Crit target for ',damage,' damage.')
    if crit==False:
        print(int(t/600),':',t/10%60,'You Hit target for ',damage,' damage.')
for t in range(1200):
    aat-=0.1
    if aat<=0:
        autoattack(t)

quit=input('enter to exit')