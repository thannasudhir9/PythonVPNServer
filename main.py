import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
import json

class VPNApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureVPN")
        self.root.geometry("800x600")
        
        # Initialize connection state
        self.connection = {
            "isConnected": False,
            "serverId": None,
            "bytesReceived": 0,
            "bytesSent": 0,
            "connectedSince": None
        }
        
        # Mock server data
        self.servers = [
            {
                "id": "1",
                "country": "Netherlands",
                "city": "Amsterdam",
                "ip": "185.65.134.201",
                "load": 45,
                "ping": 23,
                "status": "online",
                "protocol": "OpenVPN"
            },
            {
                "id": "2",
                "country": "United States",
                "city": "New York",
                "ip": "156.146.38.163",
                "load": 78,
                "ping": 98,
                "status": "online",
                "protocol": "WireGuard"
            },
            {
                "id": "3",
                "country": "Japan",
                "city": "Tokyo",
                "ip": "45.76.148.229",
                "load": 32,
                "ping": 156,
                "status": "online",
                "protocol": "OpenVPN"
            },
            {
                "id": "4",
                "country": "Germany",
                "city": "Frankfurt",
                "ip": "194.156.98.214",
                "load": 65,
                "ping": 45,
                "status": "offline",
                "protocol": "WireGuard"
            }
        ]
        
        self.setup_ui()
        self.update_stats()

    def setup_ui(self):
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=20)
        ttk.Label(title_frame, text="SecureVPN", font=("Helvetica", 24, "bold")).pack()
        
        # Connection status frame
        self.status_frame = ttk.LabelFrame(self.root, text="Connection Status")
        self.status_frame.pack(padx=20, pady=10, fill="x")
        
        # Status labels
        self.status_labels = {}
        status_grid = ttk.Frame(self.status_frame)
        status_grid.pack(padx=10, pady=5)
        
        status_items = ["Status", "Connected Time", "Downloaded", "Uploaded"]
        for i, item in enumerate(status_items):
            ttk.Label(status_grid, text=f"{item}:").grid(row=i, column=0, sticky="e", padx=5, pady=2)
            self.status_labels[item] = ttk.Label(status_grid, text="-")
            self.status_labels[item].grid(row=i, column=1, sticky="w", padx=5, pady=2)
        
        # Servers frame
        servers_frame = ttk.LabelFrame(self.root, text="Available Servers")
        servers_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Server list
        for server in self.servers:
            server_frame = ttk.Frame(servers_frame)
            server_frame.pack(padx=10, pady=5, fill="x")
            
            # Server info
            info_frame = ttk.Frame(server_frame)
            info_frame.pack(side="left")
            
            ttk.Label(info_frame, text=f"{server['city']}, {server['country']}", 
                     font=("Helvetica", 12, "bold")).pack(anchor="w")
            ttk.Label(info_frame, text=f"IP: {server['ip']}").pack(anchor="w")
            ttk.Label(info_frame, text=f"Protocol: {server['protocol']}").pack(anchor="w")
            
            # Server stats
            stats_frame = ttk.Frame(server_frame)
            stats_frame.pack(side="left", padx=20)
            
            ttk.Label(stats_frame, text=f"Ping: {server['ping']}ms").pack()
            ttk.Label(stats_frame, text=f"Load: {server['load']}%").pack()
            ttk.Label(stats_frame, text=f"Status: {server['status']}").pack()
            
            # Connect button
            btn = ttk.Button(server_frame, text="Connect",
                           command=lambda s=server: self.toggle_connection(s))
            btn.pack(side="right", padx=10)
            server['button'] = btn

    def format_bytes(self, bytes_value):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_value < 1024:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024
        return f"{bytes_value:.2f} TB"

    def format_duration(self, start_time):
        if not start_time:
            return "-"
        duration = int(time.time() - start_time)
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        if minutes > 0:
            return f"{minutes}m {seconds}s"
        return f"{seconds}s"

    def toggle_connection(self, server):
        if self.connection["isConnected"]:
            # Disconnect
            self.connection = {
                "isConnected": False,
                "serverId": None,
                "bytesReceived": 0,
                "bytesSent": 0,
                "connectedSince": None
            }
            for s in self.servers:
                s['button'].configure(text="Connect")
        else:
            # Connect
            self.connection = {
                "isConnected": True,
                "serverId": server["id"],
                "bytesReceived": 0,
                "bytesSent": 0,
                "connectedSince": time.time()
            }
            server['button'].configure(text="Disconnect")

    def update_stats(self):
        if self.connection["isConnected"]:
            self.status_labels["Status"].configure(text="Connected")
            self.status_labels["Connected Time"].configure(
                text=self.format_duration(self.connection["connectedSince"]))
            
            # Simulate data transfer
            self.connection["bytesReceived"] += 50000
            self.connection["bytesSent"] += 25000
            
            self.status_labels["Downloaded"].configure(
                text=self.format_bytes(self.connection["bytesReceived"]))
            self.status_labels["Uploaded"].configure(
                text=self.format_bytes(self.connection["bytesSent"]))
        else:
            self.status_labels["Status"].configure(text="Disconnected")
            self.status_labels["Connected Time"].configure(text="-")
            self.status_labels["Downloaded"].configure(text="-")
            self.status_labels["Uploaded"].configure(text="-")
        
        self.root.after(1000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = VPNApplication(root)
    root.mainloop()