def protocol_filter(packet, protocol):

    if protocol.lower() == "tcp" and packet.haslayer("TCP"):
        return True

    if protocol.lower() == "udp" and packet.haslayer("UDP"):
        return True

    if protocol.lower() == "icmp" and packet.haslayer("ICMP"):
        return True

    return False