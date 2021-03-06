import socket
import time
import pickle
# Socket is simply the endpoint that recieves data
# You send and recieve data to and from the socket, sitting at an ip and port

# Serialize string data


'''
Set up initial header to recieve something specific, what it is looking for.  
'''
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is IPv4 and SOCK_STREAM for TCP connections

# Bind with ip and port
s.bind((socket.gethostname(), 1238))

s.listen(5)

while True:
    clientsocket, address = s.accept()

    object_dict = {
    "name": "Pepper",
    "being": "Cat",
    "has": ['Claws', 'White paws', 'Huge Whiskers']
    }
    msg = pickle.dumps(object_dict)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    # msg = "Welcome to the server"
    # msg = f'{len(msg):<{HEADERSIZE}}' + msg

    print(f'Connection from {address} has been established')
    clientsocket.send(msg)

    """Emulate sending multiple messages """
    # while True:
    #     time.sleep(3)
    #     msg = f'It is the time {time.time()}'
    #     msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #     clientsocket.send(bytes(msg, "utf-8"))
