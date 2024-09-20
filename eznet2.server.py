import socket as s

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
port = 13001
sock.bind( ("", port) )

clmap = {}


while True:
    try:
        mess, addr = sock.recvfrom(2048)
        usr, msg = mess.decode().split("|")
        clmap[usr] = addr 
        if msg=="end":
            sock.sendto( B"SEVER|OK", addr )
            del clmap[usr]
        else:
            for _usr, _addr in clmap.items():
                if _usr != usr:
                    sock.sendto( F"{usr}>>{msg}".encode(), _addr )
    except Exception as e:
        print(e)
        break


sock.close()