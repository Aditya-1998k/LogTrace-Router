import queue
from logging.handlers import QueueHandler, QueueListener
from handlers.memory_handler import MemoryHandler

class QueueLogHandler:
    def __init__(self):
        self.log_queue = queue.Queue(-1)
        self.queue_handler = QueueHandler(self.log_queue)
        self.listner = None
        self.setup_listner()
    
    def setup_listner(self):
        handler = MemoryHandler()
        self.listner = QueueListener(self.log_queue, handler)
        self.listner.start()
    
    def get_handler(self):
        return self.queue_handler

    def stop_listner(self):
        if self.listner:
            self.listner.stop()
        