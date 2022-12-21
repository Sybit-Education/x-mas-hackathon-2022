import threading
import time
import sys


class LoadingSpinner:
    def __init__(self):
        self.stop_event = threading.Event()

    def start(self):
        # Start the spinner in a separate thread
        threading.Thread(target=self.spin, args=[]).start()

    def stop(self):
        # Stop the spinner by setting the stop event
        self.stop_event.set()

    def spin(self):
        # Display the spinner animation
        while not self.stop_event.is_set():
            for character in '|/-\\':
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.2)
                sys.stdout.write('\b')
