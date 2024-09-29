import logging
import sys

class CustomConsoleHandler(logging.StreamHandler):
    def __init__(self, stream=sys.stdout):
        super().__init__(stream)

    def emit(self, record):
        if record.levelno >= logging.ERROR:
            self.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        else:
            self.setFormatter(logging.Formatter('%(message)s'))
        super().emit(record)
