import socket
import sys
sys.path.append('/Users/taddeskorris/sandbox/python/py-security-tools')
from utils import timefunc



# from utils import timefunc

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f'Scanner {self.ip}'

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)
                print(f'Port {port} is open')

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        openports = map(str, self.open_ports)
        with open(filepath, 'w') as file:
            file.write('/n'.join(openports))


@timefunc
def main():
    ip = '192.168.1.4'
    scanner = Scanner(ip)
    print(repr(scanner))
    scanner.scan(1, 1000)
    print(scanner.open_ports)
    scanner.write('./open_ports')


if __name__ == '__main__':
    main()