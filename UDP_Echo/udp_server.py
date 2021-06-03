import socket
import pyping
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('localhost',8888))
print('Listening at {}'.format(sock.getsockname()))
addresses = set()

def run():
    while True:
        msg_bytes, address = sock.recvfrom(2048)
        addresses.add(address)
        msg_str = msg_bytes.decode('utf-8')
        if msg_str:
            msg_with_sender = f'{address[0]}:{address[1]} says: '+ msg_str
        else:
            msg_with_sender = 0
        if msg_str:
            print('{}:{} says : {}'.format(address[0],address[1], msg_str))
        # print(addresses)
        for address in addresses:
            if msg_with_sender:
                sock.sendto(msg_with_sender.encode(), address)
            # sock.sendto(str(addresses).encode(),address)

def ping(addr):
    while True:
        time.sleep(5)
        pyping.ping(addr)


a = threading.Thread()
