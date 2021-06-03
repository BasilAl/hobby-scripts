import time as t
from os import path


def createFile(dest):
    """This script creates a text file at the passed in location
    and names file based on date."""
    date = t.localtime(t.time())

    name = "{}_{}_{}.txt".format(date[2], date[1], date[0] % 100)

    if not (path.isfile(dest + name)):
        f = open(dest+name, 'w')
        f.write('\n'*30)
        f.close()


if __name__ == '__main__':
    destination = "D:\
\\Programming\\Python\\Scripts\\PyScripts\\"

    createFile(destination)
    input("done")
