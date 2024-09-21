import logging

class MemoryHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.memory = []

    def emit(self, record):
        self.memory.append(self.format(record))

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        return self.memory.clear()
