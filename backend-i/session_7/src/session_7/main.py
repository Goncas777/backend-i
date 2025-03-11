import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')



class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file  # Retornar apenas o arquivo, não a tupla

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        # Do not suppress exceptions
        self.end_time = time.perf_counter()
        logging.info(f"Time spent: {(self.end_time - self.start_time):.8f}")
        return False

# Usage example:
if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!")
