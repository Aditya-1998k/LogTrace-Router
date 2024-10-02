import logging
import os
from handlers.memory_handler import MemoryHandler
from handlers.file_handler import CustomFileHandler
from handlers.console_handler import CustomConsoleHandler
from handlers.queue_handler import QueueLogHandler
from handlers.db_handler import CustomDBLogger

handler_type = os.getenv('LOG_HANDLER', 'memory')

def create_log_handler(handler_type):
    print(handler_type)
    if handler_type == 'file':
        filename = os.getenv('FILE_NAME', 'src/logs/app.log')
        return CustomFileHandler(filename=filename)
    elif handler_type == 'console':
        return CustomConsoleHandler()
    elif handler_type == 'queue':
        return QueueLogHandler().get_handler()
    elif handler_type == 'db':
        return CustomDBLogger()
    if handler_type == 'memory':
        return MemoryHandler()

log_handler = create_log_handler(handler_type)
log_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.ERROR)

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
