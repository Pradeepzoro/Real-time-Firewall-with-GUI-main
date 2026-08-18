# 🛡️ Python Network Firewall

A modular, Python-based security tool designed to **monitor network traffic, manage access rules, and visualize packet filtering in real time**.

This project demonstrates core cybersecurity concepts such as **packet sniffing, rule-based traffic filtering, security logging, IP blacklisting, and Layer 3/4 network analysis**.

## 🚀 Features

* 🖥️ **Interactive Dashboard**
  Tkinter-based GUI for real-time network monitoring and firewall management.

* 🔐 **Dynamic Rule Engine**
  Allows or blocks network traffic based on IP addresses and specific port numbers.

* 📡 **Live Traffic Monitoring**
  Captures and analyzes network packets in real time.

* 📝 **Security Logging**
  Records network events, blocked connections, and filtering activity in `firewall.log`.

* 🚫 **Persistent IP Blacklisting**
  Stores blocked IP addresses in `blocked_ips.txt`, allowing blacklist rules to persist across sessions.

* 🌐 **Layer 3/4 Filtering**
  Analyzes network-layer and transport-layer information such as IP addresses, TCP/UDP protocols, and ports.

## 📂 Project Structure

```text
Python-Network-Firewall/
│
├── firewall_gui.py      # Graphical interface for firewall management
├── firewall.py          # Core packet interception and filtering engine
├── rules.py             # Security policies and packet validation rules
├── logger.py            # Network event and security logging utility
├── blocked_ips.txt      # Persistent list of blocked IP addresses
├── firewall.log         # Firewall activity and security logs
└── README.md            # Project documentation
```

## ⚙️ How It Works

```text
Network Traffic
       │
       ▼
 Packet Capture
       │
       ▼
 Rule Engine
       │
   ┌───┴────┐
   ▼        ▼
 ALLOW    BLOCK
   │        │
   ▼        ▼
Network   Log Event
Traffic   + Blacklist
```

The firewall captures network packets and passes them through the rule engine. The rules evaluate parameters such as **source IP, destination IP, protocol, and port number**.

Based on the configured security policies, the packet is either **allowed or blocked**. Blocked events are recorded in the security log, and restricted IP addresses can be stored for future sessions.

## 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Scapy**
* **Socket Programming**
* **File Handling**
* **Network Packet Analysis**
* **TCP/IP**
* **Linux/Windows Networking**

## 📋 Requirements

Install the required Python dependencies:

```bash
pip install scapy
```

> **Note:** Packet interception and firewall operations may require administrator/root privileges depending on your operating system.

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/Pradeepzoro/Real-time-Firewall-with-GUI-main.git
```

Navigate to the project directory:

```bash
cd Python-Network-Firewall
```

Run the GUI:

```bash
python firewall_gui.py
```

## 📊 Logging

The firewall records network activity in:

```text
firewall.log
```

Example events may include:

```text
[INFO] Packet received from 192.168.1.10
[BLOCKED] Connection from 192.168.1.25:443
[ALLOWED] Connection from 192.168.1.15:80
```

Blocked IP addresses are maintained in:

```text
blocked_ips.txt
```

## 🔒 Security Concepts Demonstrated

This project provides practical exposure to:

* Network packet sniffing
* Firewall architecture
* IP-based access control
* Port filtering
* TCP/UDP traffic analysis
* Layer 3 and Layer 4 security
* Security event logging
* IP blacklisting
* Rule-based intrusion prevention
* Real-time network monitoring

## ⚠️ Disclaimer

This project is intended for **educational and authorized security testing purposes only**.

Do not use this tool to intercept, block, or monitor network traffic on systems or networks without proper authorization.

## 🔮 Future Enhancements

* [ ] Add protocol-based filtering
* [ ] Add customizable firewall rules through the GUI
* [ ] Add traffic statistics and graphs
* [ ] Add GeoIP-based IP analysis
* [ ] Add email/security alerts
* [ ] Add whitelist management
* [ ] Add exportable security reports
* [ ] Add support for advanced intrusion detection rules

## 👨‍💻 Author

**Pradeep S**

Cybersecurity enthusiast interested in **network security, vulnerability assessment, and security automation**.

⭐ If you find this project useful, consider giving the repository a star!
