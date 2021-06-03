# This will open the configuration file and use the information there to generate the world
#roomitems is a dictionary listing the items in each room

configfile=open('houseconfig.txt')
configtext=configfile.read()
b_list=configtext.split(sep='\n')
b_room=[]
b_door=[]
b_item=[]
roomitems={}
for a in b_list:
    if a.startswith('room'):
        b_room.append(a)
        roomitems[a]=[]
    if a.startswith('door'):
        b_door.append(a)
    if a.startswith('item'):
        b_item.append(a)
        roomitems[a.split()[2]].append(a.split()[1])
    if a.startswith('start'):
        StartPos = a

for i in range(len(b_room)):
    b_room[i]=b_room[i].split()
for i in range(len(b_door)):
    b_door[i]=b_door[i].split()
for i in range(len(b_item)):
    b_item[i]=b_item[i].split()