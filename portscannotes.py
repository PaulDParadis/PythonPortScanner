#program to scan target machines to see if there are any open ports
import socket
#provides access to the BSD socket interface; it is available on all modern
#Unix systems
#The socket() function returns a socket object whose methods implement the 
#various socket system calls
# https://www.docs.python.org/3/library/socket.html
from IPy import ip
#Class and tools for handling of IPv4 and IPv6 addresses and networks
# https://www.pypi.org/project/IPy/

#Main considerations:
#1. Establish a connection to the target machine
#2. Try to connect to any open ports
#checks ip address after is input

def scan(target):
#used for scanning on ip address
    converted_ip = check_ip(target)
    print('\n' + '[- @ Scanning target] ' +str(target))
    #can scan based on either ip address or domain name
    for port in range(75, 85):
        scan_port(converted_ip, port)
        #defines range of port numbers which will be scanned in scanned_port 

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
        #converts ip function to IP format
    except ValueError:
    #returned if user emphasizes domain name
        return socket.gethostbyname()
        #converts host name to ip address

def get_banner(s):
    return s.recv(1024)
    #function for obtaining port banners
    
def scan_port(ipaddress, port):
#wrapping below code in a function makes it modulart and self-contained
    try:
        sock = socket.socket()
        #defines 'socket descriptor' invoking socket library
        sock.settimeout(0.5)
        #sets time limit for each port scanned
        sock.connect(ipaddress, port)
        try:
            banner = get_banner(sock)
            #displays port banners 
            #function using defined ip addresses and port to scan
            print('[+] Open Port ' +str(port) + ' : ' str(banner.decode().strip('\n')))
            #return message invoked if connection is successful
        except:
            print('[+] Open Port ' +str(port)) 
    except:
        pass
        #will not give output if port is closed

targets = input('[+] Enter Target/s To Scan: (split mult. targets with ,): ')
#asks user for ip address that will be included in 'sock.connect'
if ',' in targets:
    for ip add in targets.split(','):
    #used if multiple ip addresses are input
        scan(ip.add.strip(' '))
else:
    scan(targets)
