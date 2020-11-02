import scapy.all as s
from PyInquirer import prompt
from netifaces import interfaces

def main():
    interface_choices = [{'name': interface} for interface in interfaces()]
    questions = [
        dict(type='checkbox', 
        name='interfaces', 
        message='Which of the folloing interfaces do you want to sniff?',
        choices=interface_choices
        ),
    ]
    answers = prompt(questions)


if __name__ == "__main__":
    main()