from scapy.all import *

packets = sniff(iface='Ethernet', count=1000)

for i in packets:
    if('01:80:C2:00:00:0E' in str(i)):
        print('LLDP has been found it')