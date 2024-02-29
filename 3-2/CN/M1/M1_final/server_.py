import socket
import threading
import time
import logging

# Setup logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s')

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
        server_socket.listen(5)
        logging.info(f"Server listening on {host}:{port}")

        # Run the server for a fixed duration
        end_time = time.time() + duration
        while time.time() < end_time:
            client_sock, address = server_socket.accept()
            logging.info(f"Accepted connection from {address}")
            client_thread = threading.Thread(target=handle_client, args=(client_sock, stop_event))
            client_thread.start()
            threads.append(client_thread)

        stop_event.set()

    for t in threads:
        t.join()

    logging.info("Server has shut down.")

# Example usage
server_host = "0.0.0.0"
server_port = 12345

start_server(server_host, server_port, duration=60)
