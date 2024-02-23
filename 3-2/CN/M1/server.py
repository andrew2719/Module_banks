# import socket
# import threading
# import time

# def handle_client(client_socket):
#     processing_delay = 0.05  # Simulated processing delay in seconds
#     while True:
#         message = client_socket.recv(1024)
#         if not message:
#             break
#         time.sleep(processing_delay)  # Simulate processing delay
#         client_socket.sendall(message)  # Echo the message back
#     client_socket.close()

# def start_server(host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen(5)  # Listen for incoming connections
#         print(f"Server listening on {host}:{port}")
#         while True:
#             client_sock, address = server_socket.accept()
#             print(f"Accepted connection from {address}")
#             client_thread = threading.Thread(target=handle_client, args=(client_sock,))
#             client_thread.start()

# # Example usage
# server_host = "0.0.0.0"  # Listen on all network interfaces
# server_port = 12345  # Choose an appropriate port

# start_server(server_host, server_port)

import socket
import threading
import time

def handle_client(client_socket, stop_event):
    processing_delay = 0.05  # Simulated processing delay in seconds
    while not stop_event.is_set():
        message = client_socket.recv(1024)
        if not message:
            break
        time.sleep(processing_delay)  # Simulate processing delay
        client_socket.sendall(message)  # Echo the message back
    client_socket.close()

def start_server(host, port, duration=60):
    stop_event = threading.Event()
    threads = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Listen for incoming connections
        print(f"Server listening on {host}:{port}")

        # Run the server for a fixed duration
        end_time = time.time() + duration
        while time.time() < end_time:
            client_sock, address = server_socket.accept()
            print(f"Accepted connection from {address}")
            client_thread = threading.Thread(target=handle_client, args=(client_sock, stop_event))
            client_thread.start()
            threads.append(client_thread)

        stop_event.set()  # Signal all threads to stop

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Server has shut down.")

# Example usage
server_host = "0.0.0.0"  # Listen on all network interfaces
server_port = 12345      # Choose an appropriate port

start_server(server_host, server_port, duration=60)  # Run for 1 minute
