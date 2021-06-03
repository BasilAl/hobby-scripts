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
        roomitems[a.split()[1]]=[]
    if a.startswith('door'):
        b_door.append(a)
    if a.startswith('item'):
        b_item.append(a)
        roomitems[a.split()[2]].append(a.split()[1])
    if a.startswith('start'):
        StartPos = a.split()[1]
        curloc=StartPos

for i in range(len(b_room)):
    b_room[i]=b_room[i].split()
for i in range(len(b_door)):
    b_door[i]=b_door[i].split()
for i in range(len(b_item)):
    b_item[i]=b_item[i].split()




def exit():
    quit()


def help():
    print()




#This will create a list of possible moves and a list of the corresponding destinations.
lom=[]
lod=[]
lock=[]
dir=[]
for i in range(len(b_door)):
    dir.append(b_door[i][1].split(sep='-'))

for i in range(len(b_door)):
    lom.append(b_door[i][3].lower() + ' ' + dir[i][0].lower())
    lod.append(b_door[i][4])
    lock.append(b_door[i][2])

for i in range(len(b_door)):
    lom.append(b_door[i][4].lower() + ' ' + dir[i][1].lower())
    lod.append(b_door[i][3])
    lock.append(b_door[i][2])

def move(curloc, direc):
    for i in range(len(lom)):
        if (curloc.lower() + ' ' + direc.lower()) == lom[i]:
            if lock[i] == 'open':
                print('You are now in the {}'.format(lod[i].capitalize()))
                return lod[i]
            elif lock[i] == 'closed':
                print('You open the door to the {}'.format(lod[i].capitalize()))
                return lod[i]
            else:
                print('The door to the {} is locked'.format(lod[i].capitalize()))
                return curloc

def view():
    print('You are now in the {}.\n'.format(curloc.capitalize()))
    if roomitems[curloc.capitalize()] != []:
        print('You can see the following items in {}:'.format(curloc))
        for i in roomitems[curloc]:
            print(i, '\n')
            pass  # na prosthesw to use sti lista me ta items gia na deixw kai pws xrisimopoieitai
    for i in range(len(lom)):
        if lom[i].split()[0] == curloc.lower():
            print('There is a door leading {} that is {}.'.format(lom[i].split()[1].capitalize(), lock[i]))




def get_player_input():
    global curloc
    inp=input('What would you like to do next?\n')
    if inp.lower().startswith('move'):
        if (curloc.lower()+' '+inp.split()[1].lower()) in lom:
            curloc=move(curloc,inp.split()[1])
            view()
    elif inp == 'exit':
        exit()
    elif inp == 'view':
        view()


view()
while True:
   get_player_input()

