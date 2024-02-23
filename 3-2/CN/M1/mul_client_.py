import socket
import time
import random
import threading
import logging

# Setup logging
logging.basicConfig(filename='mul_client.log', level=logging.INFO, format='%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s')
# 

def calculate_transmission_speed(server_ip, server_port, message):
    message_size_bytes = len(message)
    start_time = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        sock.sendall(message.encode())
        sock.recv(1024)

    end_time = time.time()
    elapsed_time = end_time - start_time
    transmission_speed = (message_size_bytes * 8) / elapsed_time
    return transmission_speed

def send_message(server_ip, server_port, message):
    transmission_speed = calculate_transmission_speed(server_ip, server_port, message)
    transmission_delay = len(message) * 8 / transmission_speed

    propagation_delay = random.uniform(0.01, 0.05)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        start_time = time.time()
        sock.sendall(message.encode())
        sock.recv(1024)
        end_time = time.time()

    round_trip_time = end_time - start_time - propagation_delay
    end_to_end_delay = transmission_delay + propagation_delay + round_trip_time

    return {
        "Transmission Speed (bps)": transmission_speed,
        "Transmission Delay (s)": transmission_delay,
        "Propagation Delay (s)": propagation_delay,
        "Round Trip Time (s)": round_trip_time,
        "End-to-End Delay (s)": end_to_end_delay
    }

def run_client(server_ip, server_port, duration=30):
    start_time = time.time()
    while time.time() < start_time + duration:
        message = "Hello, Server!"
        delays = send_message(server_ip, server_port, message)
        logging.info(delays)

def start_multiple_clients(server_ip, server_port, thread_count=20, duration=30):
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=run_client, args=(server_ip, server_port, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Example usage
server_ip = "localhost"
server_port = 12345

start_multiple_clients(server_ip, server_port)
