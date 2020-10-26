import socket
from utils import timefunc

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def read(self, length=1024):
        pass