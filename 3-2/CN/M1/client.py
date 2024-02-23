# import socket
# import time

# def send_message(server_ip, server_port, message, transmission_speed):
#     # Size of the message in bits (assuming 1 byte = 8 bits)
#     message_size = len(message) * 8
#     transmission_delay = message_size / transmission_speed

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((server_ip, server_port))
        
#         # Simulate transmission delay
#         time.sleep(transmission_delay)

#         start_time = time.time()
#         sock.sendall(bytes(message, "utf-8"))
#         response = sock.recv(1024)
#         end_time = time.time()

#         # Simulated propagation delay
#         propagation_delay = 0.03  # Let's assume a fixed propagation delay
#         round_trip_time = end_time - start_time - propagation_delay

#         # Calculate end-to-end delay
#         end_to_end_delay = transmission_delay + propagation_delay + round_trip_time

#         return {
#             "Transmission Delay": transmission_delay,
#             "Propagation Delay": propagation_delay,
#             "Round Trip Time": round_trip_time,
#             "End-to-End Delay": end_to_end_delay
#         }

# def run_client(server_ip, server_port, duration=30, transmission_speed=1000000):
#     end_time = time.time() + duration
#     while time.time() < end_time:
#         delays = send_message(server_ip, server_port, "Hello, Server!", transmission_speed)
#         print(delays)

# # Example usage
# server_ip = "localhost"  # Use the server's IP address
# server_port = 12345  # Use the same port as the server

# run_client(server_ip, server_port)

# import socket
# import time
# import random

# def measure_transmission_speed(server_ip, server_port, test_data_size):
#     test_data = 'x' * test_data_size
#     start_time = time.time()
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((server_ip, server_port))
#         sock.sendall(test_data.encode())
#         sock.recv(1024)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     transmission_speed = (test_data_size * 8) / elapsed_time  # bits per second
#     return transmission_speed

# def send_message(server_ip, server_port, message, transmission_speed):
#     message_size = len(message) * 8  # in bits
#     transmission_delay = message_size / transmission_speed

#     propagation_delay = random.uniform(0.01, 0.05)  # Simulate varying propagation delay

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((server_ip, server_port))
#         start_time = time.time()
#         time.sleep(transmission_delay)  # Simulate transmission delay
#         sock.sendall(message.encode())
#         sock.recv(1024)
#         end_time = time.time()
#         round_trip_time = end_time - start_time - propagation_delay

#         end_to_end_delay = transmission_delay + propagation_delay + round_trip_time
#         return end_to_end_delay, transmission_delay, propagation_delay, round_trip_time

# def run_client(server_ip, server_port, duration=30):
#     # Measure transmission speed with initial test data
#     transmission_speed = measure_transmission_speed(server_ip, server_port, 1000)  # Test with 1000 bytes

#     end_time = time.time() + duration
#     while time.time() < end_time:
#         end_to_end_delay, transmission_delay, propagation_delay, round_trip_time = send_message(server_ip, server_port, "Hello, Server!", transmission_speed)
#         print(f"End-to-End Delay: {end_to_end_delay}, Transmission Delay: {transmission_delay}, Propagation Delay: {propagation_delay}, Round Trip Time: {round_trip_time}")

# # Example usage
# server_ip = "localhost"  # Replace with your server's actual IP address
# server_port = 12345  # Use the same port as the server

# run_client(server_ip, server_port)

import socket
import time
import random

def calculate_transmission_speed(server_ip, server_port, message):
    message_size_bytes = len(message)
    start_time = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        sock.sendall(message.encode())
        sock.recv(1024)  # Wait for echo response

    end_time = time.time()
    elapsed_time = end_time - start_time
    transmission_speed = (message_size_bytes * 8) / elapsed_time  # bits per second
    return transmission_speed

def send_message(server_ip, server_port, message):
    transmission_speed = calculate_transmission_speed(server_ip, server_port, message)
    transmission_delay = len(message) * 8 / transmission_speed  # Time to send the message

    propagation_delay = random.uniform(0.01, 0.05)  # Simulate varying propagation delay

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
        print(delays)

# Example usage
server_ip = "localhost"  # Replace with your server's actual IP address
server_port = 12345  # Use the same port as the server

run_client(server_ip, server_port)
