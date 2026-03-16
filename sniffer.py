from scapy.all import sniff
from parser import parse_packet

def start_sniffing():
    sniff(
        prn=parse_packet,
        store=False
    )