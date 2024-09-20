import socket as s
import threading 
import random
import sys 
import keyboard 

lock = 0b1 

def ipthndl():
    buff = []
    while True:
        evt = keyboard.read_event(True)
        if evt == keyboard.KEY_DOWN:
            if evt.name == "enter":
                sendata("".join(buff).encode())
                buff.clear()
            elif evt.name == "backspace":
                buff.pop()
            else:
                buff.append(evt.name)
        sys.stdout.write(F"\r{''.join(buff)}")
            
def rcvlock():
    while lock:
        msg = sock.recv(64).decode()
        print()
        sys.stdout.write(F"\r{msg}")
        print()






sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
#sock.bind(("", 1000+random.randint(1, 1000)))


port = 13001
svraddr = ("192.168.0.3", port)
sock.connect( svraddr )

tr = threading.Thread(target=rcvlock)
tr.start()

ilock=False
usr = s.gethostname() + F"::{random.randint(1, 10000)}"
buff = []

def bastr():
    return "".join(buff)

while True:
    sys.stdout.write(F"\r{''.join(buff)}")
    evt = keyboard.read_event(False)
    if evt.event_type == keyboard.KEY_DOWN:
        if evt.name == "enter":
            st = bastr()
            sock.send((F'{usr}|{st}'.encode()))
            if st == "end":
                lock = False
                tr.join()
                break
            buff.clear()
            print()
        elif evt.name == "backspace":
            buff.pop()
        else:
            buff.append(evt.name)

exit()
while lock:
    ilock=1
    msg = input("")
    ilock=0
    if not msg:
        continue
    data = F"{usr}|{msg}".encode()
    sock.send( data )
    if msg == "end":
        lock = False
        tr.join()
        break
sock.close()
exit()


