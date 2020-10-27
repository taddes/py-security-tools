from port_scanner import Scanner
from grabber import Grabber
from utils import timefunc

def main():
    ip = '127.0.0.1'
    scanner = Scanner(ip)
    scanner.scan(1, 1001)
    for port in scanner.open_ports:
        print(port)
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print('Error', e)

if __name__ == '__main__':
    main()