# firewall_gui.py
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import subprocess
import os
import signal

firewall_process = None

# =========================
# BUTTON FUNCTIONS
# =========================
def start_firewall():
    global firewall_process

    if firewall_process is not None:
        messagebox.showinfo("Info", "Firewall already running")
        return

    firewall_process = subprocess.Popen(
        ["sudo", "python3", "firewall.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    log_box.insert(tk.END, "🔥 Firewall started...\n")
    threading.Thread(target=read_firewall_output, daemon=True).start()

def stop_firewall():
    global firewall_process

    if firewall_process is None:
        messagebox.showinfo("Info", "Firewall not running")
        return

    firewall_process.send_signal(signal.SIGINT)
    firewall_process = None
    log_box.insert(tk.END, "Firewall stopped.\n")

def read_firewall_output():
    global firewall_process
    if firewall_process:
        for line in firewall_process.stdout:
            log_box.insert(tk.END, line)
            log_box.yview(tk.END)

def show_blocked_ips():
    try:
        with open("blocked_ips.txt", "r") as f:
            ips = f.read()
        messagebox.showinfo("Blocked IPs", ips if ips else "No blocked IPs")
    except FileNotFoundError:
        messagebox.showinfo("Blocked IPs", "No blocked IPs file found")

# =========================
# GUI DESIGN
# =========================
window = tk.Tk()
window.title("Real-Time Firewall")
window.geometry("700x500")

title = tk.Label(window, text="Real-Time Firewall Dashboard", font=("Arial", 16))
title.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

start_btn = tk.Button(button_frame, text="Start Firewall", width=15, command=start_firewall)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(button_frame, text="Stop Firewall", width=15, command=stop_firewall)
stop_btn.grid(row=0, column=1, padx=10)

block_btn = tk.Button(button_frame, text="View Blocked IPs", width=20, command=show_blocked_ips)
block_btn.grid(row=0, column=2, padx=10)

log_box = scrolledtext.ScrolledText(window, width=85, height=20)
log_box.pack(pady=15)

window.mainloop()
