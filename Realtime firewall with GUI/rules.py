BLOCKED_PORTS = [21, 22, 23, 445, 3389, 1433 ]
BLOCKED_IP_FILE = "blocked_ips.txt"

def load_blocked_ips():
    try:
        with open(BLOCKED_IP_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def check_packet(packet):
    blocked_ips = load_blocked_ips()

    if packet.haslayer("IP"):
        src_ip = packet["IP"].src

        if packet.haslayer("TCP"):
            dst_port = packet["TCP"].dport
        else:
            dst_port = None

        if src_ip in blocked_ips:
            return "BLOCK"

        if dst_port in BLOCKED_PORTS:
            return "BLOCK"

    return "ALLOW"
BLOCKED_IPS = ["192.168.1.100"]
BLOCKED_PORTS = [23, 445]

def check_packet(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src

        if packet.haslayer("TCP"):
            dst_port = packet["TCP"].dport
        else:
            dst_port = None

        if src_ip in BLOCKED_IPS:
            return "BLOCK"

        if dst_port in BLOCKED_PORTS:
            return "BLOCK"

    return "ALLOW"
