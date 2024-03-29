
import threading
import time
import queue
import random
import logging

# Setting up colored logging
class CustomFormatter(logging.Formatter):
    """ Custom formatter to add colors to log messages """
    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"
    # format = '%(message)s'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

# Configure logger
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logger.addHandler(handler)

# logging.basicConfig(level=logging.INFO, format='%(message)s')
# logger = logging.getLogger()

# class ColoredFormatter(logging.Formatter):
#     GREY = '\033[90m'
#     GREEN = '\033[92m'
#     RED = '\033[91m'
#     ORANGE = '\033[93m'
#     BLUE = '\033[94m'
#     YELLOW = '\033[33m'
#     RESET = '\033[0m'

#     FORMATS = {
#         logging.DEBUG: GREY + '%(message)s' + RESET,
#         logging.INFO: BLUE + '%(message)s' + RESET,
#         logging.ERROR: RED + '%(message)s' + RESET,
#         logging.WARNING: YELLOW + '%(message)s' + RESET,
#         logging

#         # MAC_NOT_FOUND_LEVEL: ORANGE + '%(message)s' + RESET
#     }

#     def format(self, record):
#         log_fmt = self.FORMATS.get(record.levelno, '%(message)s')
#         formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
#         return formatter.format(record)

# handler = logging.StreamHandler()
# handler.setFormatter(ColoredFormatter())
# logger.handlers = [handler]

class Router:
    def __init__(self, name, process_delay, max_queue_size, packet_loss_prob):
        self.name = name
        self.process_delay = process_delay
        self.max_queue_size = max_queue_size
        self.packet_loss_prob = packet_loss_prob
        self.queue = queue.Queue(maxsize=max_queue_size)
        self.running = True

    def process_packet(self):
        while self.running:
            try:
                packet = self.queue.get(timeout=1)
                if random.random() < self.packet_loss_prob:
                    logger.warning(f"Packet {packet} dropped at router {self.name}")
                    continue

                time.sleep(self.process_delay)
                logger.info(f"Processed packet {packet} in router {self.name}")
            except queue.Empty:
                continue

    def add_packet(self, packet):
        if not self.queue.full():
            self.queue.put(packet)
        else:
            logger.error(f"Router {self.name} is congested. Packet {packet} dropped.")

    def stop(self):
        self.running = False

class NetworkSimulator:
    def __init__(self):
        self.routers = {}
        self.total_delay = 0
        self.threads = []

    def add_router(self, name, process_delay, max_queue_size, packet_loss_prob):
        router = Router(name, process_delay, max_queue_size, packet_loss_prob)
        self.routers[name] = router
        thread = threading.Thread(target=router.process_packet)
        thread.start()
        self.threads.append(thread)

    def send_packet(self, src_router, dest_router, packet):
        if src_router in self.routers and dest_router in self.routers:
            self.total_delay += self.routers[src_router].process_delay
            self.routers[src_router].add_packet(packet)
            transmission_delay = 1
            propagation_delay = 1
            self.total_delay += transmission_delay + propagation_delay
            logger.debug(f"Total end-to-end delay for {packet}: {self.total_delay} seconds")

    def stop_simulation(self):
        for router in self.routers.values():
            router.stop()

    def wait_for_completion(self):
        for thread in self.threads:
            thread.join()

# Example usage
simulator = NetworkSimulator()
simulator.add_router("Router1", 1, 5, 0.1)
simulator.add_router("Router2", 2, 5, 0.2)

print("Sending packets...")
for i in range(100):
    # sleep 0.5 seconds
    time.sleep(0.5)
    simulator.send_packet("Router1", "Router2", f"Packet{i}")

# Run the simulation for 30 seconds and then stop
time.sleep(5)
simulator.stop_simulation()
simulator.wait_for_completion()
logger.info("Simulation ended")
