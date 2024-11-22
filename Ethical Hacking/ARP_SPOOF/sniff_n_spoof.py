from scapy.all import *

def sniff_icmp(pkt:Packet) -> None:
    icmp_type: int = pkt[ICMP].type # Getting the ICMP Type either 0 or 8
    src: str = pkt[IP].src # Getting the IP that the packet is coming from
    dst: str = pkt[IP].dst # Getting the IP that the packet is going to
    
    if icmp_type == 8:  
        print("ICMP Echo Request from %s to %s" % (src, dst))
        spoof_reply(pkt)
    elif icmp_type == 0:  
        print("ICMP Echo Reply from %s to %s" % (src, dst))

def spoof_reply(pkt:Packet) -> None:
    if pkt[ICMP].type == 8:  
        ip_layer: IP = IP(src=pkt[IP].dst, dst="10.0.0.1") # Creating the IP layer w hich takes the source IP and its target destination
        icmp_layer: ICMP = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq) # Creating the ICMP layer which needs the type, id, and seq. We're using the id and sequence given to us by the packet we're spoofing.
        spoofed_pkt = ip_layer / icmp_layer
        send(spoofed_pkt)
        print("ICMP Echo Reply (spoofed) from %s to %s" % (pkt[IP].dst,spoofed_pkt[IP].dst))
        print("\n\n")

'''
I added the 4 network interfaces after doing some investigation in ifconfig to see those were the nodes on the network.
Without the iface, the program didn't work.
'''
sniff(iface=["s1-eth1","s1-eth2","s1-eth3","s1-eth4"],filter="icmp", prn=sniff_icmp)