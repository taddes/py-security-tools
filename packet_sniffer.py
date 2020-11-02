import scapy.all as s
from PyInquirer import prompt
from netifaces import interfaces

"""
    Split out into interfaces, possibly, scan each one individually
    Capture a number of packets
    Filter the interfaces, select specific types of packets
"""

def main():
    interface_choices = [{'name': interface} for interface in interfaces()]
    questions = [
        dict(type='checkbox', 
        name='interfaces', 
        message='Which of the folloing interfaces do you want to sniff?',
        choices=interface_choices
        ),
        dict(
            type='input',
            name='timeout',
            message='How long do you want to sniff?'
        ),
        dict(
            type='confirm',
            name='save',
            message='Do you want to save the captured packets to a file?'
        )
    ]
    answers = prompt(questions)
    results = s.sniff(iface=answers['interfaces'], timeout=int(answers['timeout']))
    if answers['save']:
        print('saving')
    else:
        results.nsummary()
        s.wrpcap('capture.pcap', results)


if __name__ == "__main__":
    main()