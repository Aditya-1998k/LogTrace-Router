import logging

class MemoryHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_buffer = []

    def emit(self, record):
        self.log_buffer.append(self.format(record))

    def get_memory(self):
        return self.log_buffer

    def clear_memory(self):
        return self.log_buffer.clear()
