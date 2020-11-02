from ftplib import FTP

def main():
    host = 'localhost'
    username = 'taddes'
    password = 'password1234'

    client = FTP(host)
    client.login(username, password)
    client.dir()
    client.quit()

if __name__ == "__main__":
    main()