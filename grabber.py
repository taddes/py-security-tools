import socket
from utils import timefunc

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self,ip, self.port)

    def read(self, length=1024):
        # Read. Argument is buffer size in bytes to recieve
        # Returns the data as a bytes object
        # Used to receive data from TCP or UDP sockets
        return self.socket.recv(length)

    def close(self):
        pass