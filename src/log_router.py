import logging
import os
from handlers.memory_handler import MemoryHandler

handler  = os.getenv('LOG_HANDLER', 'memory')

def log_handler(handler):
    if handler == 'memory':
        log_handler = MemoryHandler()
    else:
        log_handler = logging.StreamHandler()
    return log_handler

log_handler = log_handler(handler)
log_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logging.getLogger().addHandler(log_handler)
logging.getLogger().setLevel(logging.DEBUG)

def write_to_logger(message, level):
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'debug':
        logging.debug(message)

def get_logs():
    return log_handler.get_memory()

def clear_logs():
    return log_handler.clear_memory()
