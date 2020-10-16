import socket

class Scanner:
    def __init__(self, ip):
        self.ip = ip

    def __repr__(self):
        return f'Scanner {self.ip}'

    def scan(self, lowerport, upperport):
        pass

    def is_open(self, port):
        pass

    def write(self, filepath):
        pass

def main():
    ip = '192.168.1.5'
    scanner = Scanner(ip)
    print(repr(scanner))


if __name__ == '__main__':
    main()