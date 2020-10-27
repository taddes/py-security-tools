import os

def main():
    
    user =  os.getenv('USER')
    if user is not None:
        print(user)

    second = os.environ.get('USERNAME', 'nothing')
    print(second)

if __name__ == "__main__":
    main()