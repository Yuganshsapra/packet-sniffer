from scapy.layers.inet import IP, TCP, UDP, ICMP
from utils import format_output
from logger import log_packet

def parse_packet(packet):

    if IP in packet:

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        src_port = None
        dst_port = None
        proto_name = "UNKNOWN"

        if TCP in packet:
            proto_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif UDP in packet:
            proto_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif ICMP in packet:
            proto_name = "ICMP"

        packet_size = len(packet)

        output = format_output(
            proto_name,
            src_ip,
            dst_ip,
            src_port,
            dst_port,
            packet_size
        )

        print(output)

        log_packet(output)