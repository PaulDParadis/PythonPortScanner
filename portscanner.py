#Portscanner project
import socket
from IPy import IP
#establish connection with target machine
#see if port is open
#socket library allows us to establish a connection over the internet
def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[- 0 Scanning Target]' + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        Ip(ip)
        return(ip)
    except Valueerror:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress. port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

targets = input('[+] Enter target/s to scan (split multiple targets with ,)')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
