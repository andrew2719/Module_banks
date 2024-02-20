import threading
import random
import time
import logging

class Node(threading.Thread):
    def __init__(self, ip, mac, network):
        super().__init__()
        self.ip = ip
        self.__mac = mac
        self.network = network
        self.stop_signal = threading.Event()

    def get_mac(self):
        return self.__mac

    def run(self):
        while not self.stop_signal.is_set():
            # Sending messages to a random node
            dst_ip = f"10.10.10.{random.randint(1, 6)}"
            self.network.send_message(self.ip, dst_ip, f"Hello from {self.ip} to {dst_ip}")
            time.sleep(random.uniform(1, 3))  # Random wait time between messages

    def stop(self):
        self.stop_signal.set()

class ARPTable:
    def __init__(self):
        self.table = {}

    def add_entry(self, ip, mac):
        self.table[ip] = mac

    def get_mac(self, ip):
        return self.table.get(ip, None)

    def print_table(self):
        for ip, mac in self.table.items():
            print(f"IP: {ip}, MAC: {mac}")

class Switch:
    def __init__(self, nodes):
        self.arp_table = ARPTable()
        self.nodes = nodes
        self.transmit_lock = threading.Lock()
        self.collision_detected = False
        print("Switch created")

    def discover_mac(self, ip):
        for node in self.nodes:
            if node.ip == ip:
                self.arp_table.add_entry(ip, node.get_mac())
                print(f"Discovered MAC: {node.get_mac()} for IP: {ip}")
                break

    def send_message(self, src_ip, dst_ip, data):
        with self.transmit_lock:
            if self.collision_detected:
                print(f"Collision detected for message from {src_ip}. Backing off...")
                time.sleep(random.uniform(1, 2))  # Random backoff
                self.collision_detected = False
                return

            if random.random() < 0.3:  # 30% chance of another node transmitting
                self.collision_detected = True

            mac = self.arp_table.get_mac(dst_ip)
            if not mac:
                print(f"MAC address for IP {dst_ip} not found, initiating discovery...")
                self.discover_mac(dst_ip)
            else:
                print(f"Found MAC: {mac} for IP: {dst_ip}")
                print(f"Sending message from {src_ip} to {dst_ip}: {data}")
            self.arp_table.print_table()

class Network:
    def __init__(self, nodes):
        self.switch = Switch(nodes)

    def send_message(self, src_ip, dst_ip, data):
        self.switch.send_message(src_ip, dst_ip, data)

# Nodes creation
nodes = [
    Node(ip="10.10.10.1", mac="00:00:00:00:00:01", network=None),
    Node(ip="10.10.10.2", mac="00:00:00:00:00:02", network=None),
    Node(ip="10.10.10.3", mac="00:00:00:00:00:03", network=None),
    Node(ip="10.10.10.4", mac="00:00:00:00:00:04", network=None),
    Node(ip="10.10.10.5", mac="00:00:00:00:00:05", network=None),
    Node(ip="10.10.10.6", mac="00:00:00:00:00:06", network=None)
]

# Network setup
network = Network(nodes)
for node in nodes:
    node.network = network
    node.start()

# Run the simulation for a certain duration
time.sleep(30)  # Duration of the simulation in seconds

# Stop all nodes
for node in nodes:
    node.stop()
    node.join()

