import socket as s
import threading 


def rcvlock():
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
sock.connect( ("172.20.10.5", 12000) )
t = threading.Thread(target=rcvlock)
t.start()

usr = input("usr>> ")


while True:
    msg = input(">>")
    msg=f'{usr}|{msg}'
    sock.send(msg.encode())



sock.close()

