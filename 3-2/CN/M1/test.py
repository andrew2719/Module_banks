
class Node:
    def __init__(self, ip, mac):
        self.ip = ip
        self.__mac = mac

    def get_mac(self):
        return self.__mac

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
        print("Switch created")

    def discover_mac(self, ip):
        for node in self.nodes:
            if node.ip == ip:
                self.arp_table.add_entry(ip, node.get_mac())
                print(f"Discovered MAC: {node.get_mac()} for IP: {ip}")
                break

    def find_mac(self, ip):
        mac = self.arp_table.get_mac(ip)
        if not mac:
            print(f"MAC address for IP {ip} not found, initiating discovery...")
            self.discover_mac(ip)
        else:
            print(f"Found MAC: {mac} for IP: {ip}")

    def print_table(self):
        self.arp_table.print_table()

class Message:
    def __init__(self, src_ip, dst_ip, data):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.data = data

class Network:
    def __init__(self, nodes):
        self.switch = Switch(nodes)

    def send_message(self, src_ip, dst_ip, data):
        print(f"Sending message from {src_ip} to {dst_ip}: {data}")
        self.switch.find_mac(dst_ip)
        mac = self.switch.arp_table.get_mac(dst_ip)
        if mac is not None:
            message = Message(src_ip, dst_ip, data)
            print(f"Message sent: {message.data}")
        else:
            print(f"IP {dst_ip} not found in ARP table")
        self.switch.print_table()

# Nodes creation
nodes = [
    Node(ip="10.10.10.1", mac="00:00:00:00:00:01"),
    Node(ip="10.10.10.2", mac="00:00:00:00:00:02"),
    Node(ip="10.10.10.3", mac="00:00:00:00:00:03"),
    Node(ip="10.10.10.4", mac="00:00:00:00:00:04"),
    Node(ip="10.10.10.5", mac="00:00:00:00:00:05"),
    Node(ip="10.10.10.6", mac="00:00:00:00:00:06")
]

# Network setup
network = Network(nodes)

# Simulation of message sending
network.send_message("10.10.10.1", "10.10.10.2", "Hello, Node 2!")
