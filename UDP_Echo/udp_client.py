import socket

address=('127.0.0.1',8888)
client_address = ('localhost',8889)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(client_address)
sock.settimeout(100)
sock.sendto((str(client_address)+" connected").encode('utf-8'),address)
while True:
    data,addr = sock.recvfrom(2048)
    while data:
        text=data.decode('utf-8')
        data = 0
        print('received from server {0}:{1} : {2}'.format(addr[0],addr[1],text))
    data = input('>')
    sock.sendto(data.encode('utf-8'),address)
