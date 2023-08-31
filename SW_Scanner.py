from scapy.all import sniff
from scapy.all import load_contrib

load_contrib('cdp')

class main:
    def __init__(self):
        self.filter = "ether host 01:00:0c:cc:cc:cc"
        try:
            self.p = sniff(count=1,iface='Ethernet',filter=self.filter,timeout=60)
        except:
            print('OUCH!  Something went wrong.')
        else:
            print('Finished processing...')
            print("DeviceID: {}".format(self.p[0].payload["CDPMsgDeviceID"].val.decode('utf-8')))
            print("PortID: {}".format(self.p[0].payload["CDPMsgPortID"].iface.decode('utf-8')))
            print("NativeVLAN: {}".format(self.p[0].payload["CDPMsgNativeVLAN"].vlan))
            print("IPv4addr: {}".format(self.p[0].payload["CDPAddrRecordIPv4"].addr))
            print("Model: {}".format(self.p[0].payload["CDPMsgPlatform"].val.decode('utf-8')))
            print("Duplex: {}".format(self.p[0].payload["CDPMsgDuplex"].duplex))
            print("VTP Domain: {}".format(self.p[0].payload["CDPMsgVTPMgmtDomain"].val.decode('utf-8')))

if __name__ == "__main__": main()