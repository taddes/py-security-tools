import argparse
from ipaddress import ip_interface

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-a', '--address', help='host address', required=True)
    # parser.add_argument('-m', '--mask', help='mask', required=True)
    # parser.parse_args()

    host = '192.168.0.1'
    mask = '29'
    iface = ip_interface(f"{host}/{mask}")
    broadcast = iface.network.broadcast_address
    network = iface.network.network_address
    hostmask = iface.hostmask
    netmask = iface.netmask
    hosts = list(iface.network.hosts())
    minimum_host = min(hosts, default=None)
    maximum_host = max(hosts, default=None)
    print(f"""
    Network:            {network}/{mask}
    Netmask:            {netmask}
    Broadcast:          {broadcast}
    Min Host:           {minimum_host}
    Max Host:           {maximum_host}
    Hosts per Network:  {str(len(host))}
    """)
    print('Hosts:')
    for h in hosts:
        print(h)

if __name__ == "__main__":
    main()