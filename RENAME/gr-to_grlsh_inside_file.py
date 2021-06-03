import os

os.chdir("C:/Users/alift/Desktop/RenameTestFolder/RenameInsideFolder")
print(os.getcwd())
for s in os.listdir():
    print(s)


mitsos = open("C:/Users/alift/Desktop/listxt.txt", "r", encoding="UTF-8").read().split(sep="\n")

print(mitsos)
a = []
for i in mitsos:
    b = i.split(sep="|")
    a.append(b)
print(a)
name = []
name_dash = []
rename = []
for n in a:
    if len(n) == 3:
        name.append(n[0])
        name_dash.append(n[1])
        rename.append(n[2])

print()
print(name)
print()
print(name_dash)
print()
print(rename)

name_rename = []
for i in range(len(name)):
    name_rename.append((name[i], rename[i]))

for s in os.listdir():
    takis = open("C:/Users/alift/Desktop/RenameTestFolder/RenameInsideFolder/"+s, "r+").read()
    for bit in name_rename:
        if bit[0] in takis:
            takis.replace(bit[0], bit[1])
