
from scapy.all import sniff, IP, TCP, UDP
from rules import check_packet
from logger import log_event
import time
from collections import defaultdict
import os


TIME_WINDOW = 10          
PACKET_RATE_LIMIT = 40   
PORT_HIT_LIMIT = 25      
DOS_SCORE_LIMIT = 2      

BLOCKED_IP_FILE = "blocked_ips.txt"


ip_packets = defaultdict(list)
ip_ports = defaultdict(list)
blocked_ips = set()


if os.path.exists(BLOCKED_IP_FILE):
    with open(BLOCKED_IP_FILE, "r") as f:
        blocked_ips = set(line.strip() for line in f if line.strip())


def auto_block_ip(ip, reason):
    if ip not in blocked_ips:
        blocked_ips.add(ip)
        with open(BLOCKED_IP_FILE, "a") as f:
            f.write(ip + "\n")
        print(f" AUTO-BLOCKED IP: {ip} | Reason: {reason}")

def detect_dos(ip):
    score = 0


    if len(ip_packets[ip]) > PACKET_RATE_LIMIT:
        score += 1


    if ip_ports[ip]:
        most_targeted_port = max(set(ip_ports[ip]), key=ip_ports[ip].count)
        if ip_ports[ip].count(most_targeted_port) > PORT_HIT_LIMIT:
            score += 1


    if len(ip_packets[ip]) > PACKET_RATE_LIMIT * 1.5:
        score += 1

    return score >= DOS_SCORE_LIMIT


def process_packet(packet):
    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src
    current_time = time.time()


    if src_ip in blocked_ips:
        log_event(packet, "BLOCKED (BLACKLISTED IP)")
        return


    ip_packets[src_ip].append(current_time)
    ip_packets[src_ip] = [
        t for t in ip_packets[src_ip]
        if current_time - t <= TIME_WINDOW
    ]


    if packet.haslayer(TCP):
        ip_ports[src_ip].append(packet[TCP].dport)
    elif packet.haslayer(UDP):
        ip_ports[src_ip].append(packet[UDP].dport)


    if detect_dos(src_ip):
        print(f"🔥 DOS DETECTED → IP BLOCKED: {src_ip}")


        log_event(
            packet,
            f"DOS ATTACK DETECTED | Auto-blocked IP {src_ip}"
        )

        auto_block_ip(src_ip, "Rate + Port Abuse")
        return


    decision = check_packet(packet)

    if decision == "BLOCK":
        print(" BLOCKED:", packet.summary())
        log_event(packet, "BLOCKED (RULE MATCH)")
        return

    print("ALLOWED:", packet.summary())


print("Real-Time Firewall with DoS Detection Started...")
sniff(prn=process_packet, store=False)

