import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate():
    temp = ''
    for i in range(2):
        for i in range(3):
            temp += random.choice(digits)
        for i in range(3):
            temp += random.choice(letters)
    temp += '@hpeprint.com'
    return temp


mails = []
for i in range(10):
    mails.append(generate())

for i in range(len(mails)):
    print(mails[i])
