def move(curloc,direc):
    for i in range(len(lom)):
        if (curloc+' '+direc) in lom:
            if lock[i]=='open':
                curloc=lod[i]
                print('You are now in the {}'.format(curloc))
            elif lock[i]=='closed':
                curloc=lod[i]
                print('You open the door to the {}'.format(curloc))
            else:
                print('The door to the {} is locked'.format(lod[i]))

def exit():
    quit()

def help():
    print()

def view():
    print('You are now in {}.\n'format(curloc))
    if roomitems[curloc] != []:
        print('You can see the following items in {}:\n'.format(curloc))
        for i in roomitems[curloc]:
            print(i,'\n')
            pass #na prosthesw to use sti lista me ta items gia na deixw kai pws xrisimopoieitai
    for i in range(len(lom)):
        if lom[i].split()[0]==curloc:
            print('There is a door leading {} that is {}.\n'.format(lom[i].split[1],lock[i]))
