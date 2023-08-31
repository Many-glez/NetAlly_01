from scapy.all import *

load_contrib('lldp')

packets = sniff(iface='Ethernet',count=500)

lldp_address = "01:80:c2:00:00:0e"

for i in packets:
    if(lldp_address in str(i)):
        print('===============================\n')
        #print('System Name: {}'.format(packets[0].payload["LLDPDUSystemName"].system_name.decode('utf-8')))    
        #print(packets[0].payload['LLDPDUPortDescription'].value.decode('utf-8'))
        print(i.tlvlist[0].chassis_id)
        #print(packets[0].payload['LLDPUManagementAddress'].value.decode('utf-8'))
        print('\n===============================\n')

'''def lldp_packet_handler(pkt):
    lldp = "01:80:c2:00:00:0e"
    if lldp in str(pkt):
        print("LLDP Packet Detected")
        print("Chassis ID: ", pkt[lldp].tlvlist[0].chassis_id)
        print("Port ID: ", pkt[lldp].tlvlist[1].port_id)
        # Add more attributes as needed

def main():
    iface = "Ethernet"  # Specify the interface you want to capture on
    sniff(iface=iface, prn=lldp_packet_handler, count=200)

if '__name__' == "__main__":
    main()
'''