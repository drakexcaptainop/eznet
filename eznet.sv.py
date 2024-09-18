import socket as s
import threading

def gipv4():
    hostname = s.gethostname()
    ip_address = s.gethostbyname(hostname)
    return ip_address
def accl():
    while True:
        T = sock.accept()
        cls.append(T[1])



ip = gipv4()
cls = []

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
sock.bind(('',12000))

clmap = {}


while True:
    data, client_address = sock.recvfrom(1024) 
    usr, msg = data.decode().split('|')
    clmap[usr] = client_address
    print(f'{usr}>> {msg}')
    for cusr, addr in clmap.items():
        if cusr != usr:
            sock.sendto(f'{usr}>> {msg}'.encode(), addr)

