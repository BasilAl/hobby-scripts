import os


char_migrate = {
    "ς": 's',
    'ε': 'e', 'ρ': 'r', "τ": "t", "υ": "y", "θ": "th", "ι": "i", "ο": "o", "π": "p", "α": "a",
    "σ": "s", "δ": "d", "φ": "f", "γ": "g", "η": "i", "ξ": "x", "κ": "k", "λ": "l",
    "ζ": "z", "χ": "x", "ψ": "ps", "ω": "o", "β": "v", "ν": "n", "μ": "m",
    "Ε": "e", "Ρ": "r", "Τ": "t", "Υ": "y", "Θ": "th", "Ι": "i", "Ο": "o", "Π": "p", "Α": "a",
    "Σ": "s", "Δ": "d", "Φ": "f", "Γ": "g", "Η": "i", "Ξ": "x", "Κ": "k",
    "Λ": "l", "Ζ": "z", "Χ": "x", "Ψ": "ps", "Ω": "o", "Β": "v", "Ν": "n", "Μ": "m",
    "Έ": "e", "Ά": "a", "Ύ": "y", "Ί": u"i", u"Ό": u"o", "Ή": u"i", "Ώ": u"o",
    "έ": u"e", "ά": u"a", "ύ": u"y", "ί": u"i", "ό": u"ο", "ή": u"i", "ώ": u"o",
    "ϋ": u"i", "ϊ": u"i", "ΐ": u"i", "ΰ": u"i",
    "Ϊ": u"i", "Ϋ": u"i", u"á": "a", "ó": "o"
}


#Example in folder
os.chdir('C:/Users/alift/Desktop/RenameTestFolder')
#listxt = open("C:/Users/alift/Desktop/listxt.txt", "w", encoding="UTF-8")
for f in os.listdir():
    name = f
    new_name = ""
    # print(f)
    for l in name:
        if l in char_migrate:
            b = char_migrate[l]
            new_name += b
        else:
            new_name += l
    #dashed_name = new_name.replace(" ", "-")
    # listxt.write(name+"|"+dashed_name+"|"+new_name+"\n")
    os.rename(f, new_name)
# listxt.close()


'''
mitsos = open("C:/Users/alift/Desktop/listxt.txt", "r", encoding="UTF-8").read().split(sep="\n")

print(mitsos)
a = []
for i in mitsos:
    b = i.split(sep="|")
    a.append(b)
print()
print()
print(a)
'''
