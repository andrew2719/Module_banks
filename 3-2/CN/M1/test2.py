import threading
import random
import time

class Node(threading.Thread):
    def __init__(self, ip, mac, network):
        super().__init__()
        self.ip = ip
        self.mac = mac
        self.network = network
        self.stop_signal = threading.Event()

    def run(self):
        while not self.stop_signal.is_set():
            self.network.send_message(self.ip, "10.10.10.255", "Hello from " + self.ip)
            time.sleep(random.uniform(1, 3))  # Random wait time between messages

    def stop(self):
        self.stop_signal.set()

class Network:
    def __init__(self, nodes):
        self.nodes = nodes
        self.transmit_lock = threading.Lock()
        self.collision_detected = False

    def send_message(self, src_ip, dst_ip, data):
        with self.transmit_lock:
            if self.collision_detected:
                print(f"Collision detected for message from {src_ip}. Backing off...")
                time.sleep(random.uniform(1, 2))  # Random backoff
                self.collision_detected = False
                return

            # Simulate other nodes sending at the same time
            if random.random() < 0.3:  # 30% chance of another node transmitting
                self.collision_detected = True

            print(f"Sending message from {src_ip} to {dst_ip}: {data}")
            time.sleep(1)  # Slow down the simulation

# Nodes creation
nodes = [
    Node(ip="10.10.10.1", mac="00:00:00:00:00:01", network=None),
    Node(ip="10.10.10.2", mac="00:00:00:00:00:02", network=None),
    # Add other nodes here...
]

# Network setup
network = Network(nodes)
for node in nodes:
    node.network = network
    node.start()

# Add logic to terminate the simulation after a certain duration
time.sleep(30)  # Run the simulation for 30 seconds

for node in nodes:
    node.stop()
    node.join()
