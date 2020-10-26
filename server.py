import socket
# Socket is simply the endpoint that recieves data
# You send and recieve data to and from the socket, sitting at an ip and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is IPv4 and SOCK_STREAM for TCP connections

# Bind with ip and port
s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established')
    clientsocket.send(bytes("Welcome to the server", "utf-8"))