import logging
import os
from handlers.memory_handler import MemoryHandler
from handlers.file_handler import CustomFileHandler

handler_type = os.getenv('LOG_HANDLER', 'memory')

def create_log_handler(handler_type):
    if handler_type == 'memory':
        return MemoryHandler()
    else:
        filename = os.getenv('FILE_NAME', 'src/logs/app.log')
        return CustomFileHandler(filename=filename)

log_handler = create_log_handler(handler_type)
log_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

def write_to_logger(message, level):
    if level == 'info':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'debug':
        logger.debug(message)

def get_logs():
    if hasattr(log_handler, 'get_memory'):
        return log_handler.get_memory()
    return []

def clear_logs():
    if hasattr(log_handler, 'clear_memory'):
        return log_handler.clear_memory()