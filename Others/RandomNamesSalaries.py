import random

"""Generates a list of random names of people who owe money to the treasury. Also generates random salaries and random
 amounts of money owed. Was part of creating a mock database for a university project. I think I lost the other parts 
 of thescript."""


def listNames(amount):
    '''generate "amount" random names and return a list of them'''

    mikra_m = (
        "mitsos", "giorgos", "takis", "xristoforos", "sokratis", "lefteris",
        "vasilis", "lakis", "makis", "sotiris", "kostas", "konstantinos",
        "dimitris", "alexandros", "xristos", "giannis", "stratos", "lampros",
        "fotis", "panagiotis", "anastasis", "savvas", "paraskevas", "menelaos", "vaggelis", "zachos"

    )
    mikra_f = ("alexandra", "sofia", "maria", "katerina", "ioanna", "giota", "lamprini",
               "georgia", "polyxeni", "anna", "konstantina", "vaso", "persefoni", "foteini",
               "irida", "eirini", "areti", "marianthi", "sotiria", "elissavet", "nikoleta",
               "spyridoula", "georgianna", "charitini", "evanthia", "electra", "paraskevi"

               )
    epitheta_m = (
        "donganos", "tsoukalas", "karamitros", "karapanagis", "kitsos", "papamichail",
        "papastratos", "efstathiadis", "avramidis", "aggelidis", "athanasiou",
        "alafouzos", "argyros", "vasileiadis", "vasilopoulos", "vilaetis",
        "galanopoulos", "georgiou", "goudis", "daskalakis", "doxaras", "eleftheropoulos",
        "zografos", "thanos", "ioannidis", "kakridis", "kalogiannis", "kechagias",
        "konstantopoulos", "lazopoulos", "liapis", "manousis", "mpezos", "mylwnas",
        "nastos", "nakos", "michailidis", "mitsotakis", "oikonomakos", "oikonomidis",
        "papageorgiou", "papadimas", "papadimoulis", "papakonstantinou", "papachristos",
        "poulopoulos", "raptis", "sideris", "samaras", "spanos", "spanoudakis", "stephanopoulos",
        "stefanakis", "stamos", "tsakonas", "tsakalwtos", "tsiklitiras", "flwros", "fwtopoulos",
        "xristopoulos", "christodoulopoulos", "chatzipavlou", "xatzipavlos", "stylios"
    )

    epitheta_f = (
        "donganou", "tsoukala", "karamitrou", "karapanagi", "kitsou", "papamichail",
        "papastratou", "efstathiadi", "avramidi", "aggelidi", "athanasiou",
        "alafouzou", "argyrou", "vasileiadi", "vasilopoulou", "vilaeti",
        "galanopoulou", "georgiou", "goudi", "daskalaki", "doxara", "eleftheropoulou",
        "zografou", "thanou", "ioannidi", "kakridi", "kalogianni", "kechagia",
        "konstantopoulou", "lazopoulou", "liapi", "manousi", "mpezou", "mylwna",
        "nastou", "nakou", "michailidi", "mitsotaki", "oikonomakou", "oikonomidi",
        "papageorgiou", "papadima", "papadimouli", "papakonstantinou", "papachristou",
        "poulopoulou", "rapti", "sideri", "samara", "spanou", "spanoudaki", "stephanopoulou",
        "stefanaki", "stamou", "tsakona", "tsakalwtou", "tsiklitira", "flwrou", "fwtopoulou",
        "xristopoulou", "christodoulopoulou", "chatzipavlou", "styliou"
    )

    a = []
    for i in range(amount):
        if random.random() < 0.5:
            t = str(epitheta_m[random.randint(0, len(epitheta_m)-1)]).capitalize() + \
                " "+str(mikra_m[random.randint(0, len(mikra_m)-1)]).capitalize()
            a.append(t)
        else:
            t = epitheta_f[random.randint(0, len(epitheta_f)-1)].capitalize()+" " + \
                mikra_f[random.randint(0, len(mikra_f)-1)].capitalize()
            a.append(t)
    return a

'''
b=listNames(200)
for i in b:
    print(i)
'''
a=listNames(1500)

b="{"
for i in range(len(a)):
    b+='"'+a[i]+'"'
    if i!=(len(a)-1):
        b+=","
b+="}"
#print(b)
#b=onoma
#c=paidia
#d=polyteknos
#e=income
#f=debt

c="{"
d="{"
for i in range(1500):
    j=random.randint(0,5)
    if j>2:
        j=random.randint(0,5)
        if j>3:
            j=random.randint(0,5)
    if j>3:
        d+="1"
    else:
        d+="0"
    c+=str(j)
    if i!=1499:
        c+=","
        d+=","
c+="}"
d+="}"

e="{"
f="{"
for i in range(1500):
    j=random.randint(24,600)
    if j<70:
        j=random.randint(24,600)
        if j<70:
            j=random.randint(24,600)
            if j>500:
                j=random.randint(24,600)
    elif j>300:
        j=random.randint(24,600)
        if j>300:
            j=random.randint(24,600)
            if j>500:
                j=random.randint(24,600)
    else:
        pass
    income=str(j*100)
    t=random.randint(1,70)
    if t>30:
        t=random.randint(1,75)
        if t>50:
            t=random.randint(1,75)
    debt=str(j*t*25)
    e+=income
    f+=debt
    if i!=1499:
        e+=","
        f+=","
e+="}"
f+="}"


#print(b)#onoma
#print(c)#paidia
print("\n"*3)
#print(d)#polyteknos
print(e)#eisodima
print("\n"*3)
print(f)#xreos
