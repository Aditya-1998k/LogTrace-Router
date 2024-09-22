import logging

class MemoryHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_buffer = []

    def emit(self, record):
        log_entry = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': self.format(record)  # Ensure you use a proper formatter
        }
        self.log_buffer.append(log_entry)

    def get_memory(self):
        return self.log_buffer

    def clear_memory(self):
        return self.log_buffer.clear()
