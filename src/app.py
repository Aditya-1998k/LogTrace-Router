from flask import Flask, jsonify
import logging
from handlers.memory_handler import MemoryHandler
app = Flask(__name__)

memory_handler = MemoryHandler()
memory_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
memory_handler.setFormatter(formatter)

logging.getLogger().addHandler(memory_handler)
logging.getLogger().setLevel(logging.DEBUG)

@app.route('/hello', methods=['GET'])
def hello_world():
    try:
        logging.info('Hello, World! Executed')
        return "Hello, World!", 200
    except Exception as e:
        logging.error(f'Error: {e}')
        return "Error", 500

@app.route('/log', methods=['GET'])
def get_buffer_log():
    logs = memory_handler.get_memory()
    return jsonify(logs)

if __name__ == '__main__':
    logging.info('Starting server')
    app.run(host='0.0.0.0', port=5000)