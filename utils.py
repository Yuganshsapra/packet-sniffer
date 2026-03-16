def format_output(protocol, src_ip, dst_ip, src_port, dst_port, size):

    output = "\n--- Packet Captured ---\n"
    output += f"Protocol: {protocol}\n"
    output += f"Source IP: {src_ip}\n"
    output += f"Destination IP: {dst_ip}\n"

    if src_port:
        output += f"Source Port: {src_port}\n"

    if dst_port:
        output += f"Destination Port: {dst_port}\n"

    output += f"Packet Size: {size} bytes\n"

    return output