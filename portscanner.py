#Portscanner project
import socket
from IPy import IP
#establish connection with target machine
#see if port is open
#socket library allows us to establish a connection over the internet

port = 80

def scan port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress. port))
        print('[+] Port '+ str(port) +' is open.')
    except:
        print('[+] Port '+ str(port) +' is closed.')

ipaddres = input('[+] Enter target to scan: ')

for port in range(1, 10):
    scan_port(ipaddress, port)
