import pytest
import logging

from handlers.memory_handler import MemoryHandler

@pytest.fixture
def setup_logging():
    memory_handler = MemoryHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    memory_handler.setFormatter(formatter)

    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)
    logger.addHandler(memory_handler)

    yield logger, memory_handler

def my_function():
    logger = logging.getLogger('my_logger')
    logger.info("This is a log from my_function.")

def test_logging(setup_logging, caplog):
    logger, memory_handler = setup_logging

    # A built-in pytest fixture that captures log messages during the test.
    with caplog.at_level(logging.INFO):
        my_function()

    # Assert that the log was captured
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[0].message == "This is a log from my_function."
    
    # check the memory handler
    assert len(memory_handler.get_memory()) == 1
    assert memory_handler.get_memory()[0]['message'] == "This is a log from my_function."
