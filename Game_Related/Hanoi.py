# Hanoi algorithm

def Move(frm, to):
    print("Move from {} to {}".format(frm, to))


def Hanoi(n, frm, aux, to):
    if n == 1:
        Move(frm, to)
    else:
        Hanoi(n-1, frm, to, aux)
        Move(frm, to)
        Hanoi(n-1, aux, frm, to)


Hanoi(4, 'A', 'B', 'C')
