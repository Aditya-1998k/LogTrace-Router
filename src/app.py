from flask import Flask
import logging
from handlers.memory_handler import MemoryHandler
app = Flask(__name__)

memory_handler = MemoryHandler()
memory_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
memory_handler.setFormatter(formatter)

logging.getLogger().addHandler(memory_handler)
logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['GET'])
def hello_world():
    logging.info('Hello, World! Executed')
    return "Hello, World!", 200

@app.route('/memory', methods=['GET'])
def get_memory():
    return {"memory": memory_handler.get_memory()}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)