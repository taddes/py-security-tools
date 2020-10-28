"""
Docs: https://www.paramiko.org/
"""
from paramiko import SSHClient
from paramiko.client import AutoAddPolicy

def main():
    with SSHClient() as client:
        # First time you make connection, you are queried to add policy
        # Paramiko doesn't auto add if host not known
        # Will add to known hosts
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect('192.168.1.15', username='admin', password='xxxxx')

        # File system
        stdin, stdout, stderr = client.exec_command('ls -l')
        output = stdout.read()
        # Must decode as a binary stream
        print(output.decode())


if __name__ == "__main__":
    main()