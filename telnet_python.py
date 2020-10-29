"""
ssh -i
begin Telnet instance on server prior to attempt
sudo systemctl start telnet.socket
"""
from getpass import getpass
from telnetlib import Telnet

def main():
    host = '192.164.1.1'
    user = 'admin'
    password = getpass()
    client = Telnet(host)
    client.read_until(b'login: ')
    client.write(user.encode() + b'\n')
    if password:
        client.read_until(b'Password: ')
        client.write(password.encode() + '\n')
        print(client.read_some().decode())
    client.write(b'ls -lah/\n')
    client.write(b'exit \n')
    print(client.read_all().decode())

if __name__ == "__main__":
    main()