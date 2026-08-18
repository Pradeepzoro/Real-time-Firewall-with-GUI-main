# Real-time-Firewall-with-GUI-main
A modular, Python-based security tool designed to monitor network traffic, manage access rules, and provide real-time visualization of packet filtering.This project demonstrates core cybersecurity concepts including packet sniffing, rule-based filtering, and security logging.
🚀 Features
Interactive Dashboard: A Tkinter-based GUI for real-time monitoring and easy management.
Dynamic Rule Engine: Custom logic to allow or block traffic based on IP addresses and specific ports
Live Traffic Logging: Detailed capture of network events stored in firewall.log for forensic analysis.
Persistent Blacklisting: Automatically saves blocked entities to blocked_ips.txt to maintain security across sessions.
Layer 3/4 Filtering: Ability to intercept and analyze packets at the network and transport layers.
📂 Project Structure
File	Description
firewall_gui.py	The main graphical interface for starting the firewall and viewing logs.
firewall.py	The core backend engine that handles packet interception and filtering logic.
rules.py	Defines the security policies and validates incoming packets against set criteria.
logger.py	Utility for writing network events and blocked attempts to the log file.
blocked_ips.txt	A persistent database of restricted IP addresses.
