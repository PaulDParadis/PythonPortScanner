#Portscanner project
import socket
from IPy import IP
#establish connection with target machine
#see if port is open
#socket library allows us to establish a connection over the internet


class PortScan():
    banners = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = self.target
        self.port_num = self.port_num

    def scan(self):
        for port in range(1, 100):
            scan_port(port)

    def check_ip(self):
        try:
            Ip(self.target)
            return(self.target)
        except Valueerror:
            return socket.gethostbyname(self.target)

    def scan_port(self.port):
        try:
            converted_ip = self.check_ip()
            sock = self.socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banners)
            except:
                self.banners.append('[ ]') 
            sock.close()
                
        except:
            pass

