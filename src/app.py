from flask import Flask, jsonify
import logging
from log_router import write_to_logger, get_logs, clear_logs
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    try:
        write_to_logger('Hello, World! Executed', level='Warning')
        a = 1/0
        return "Hello, World!", 200
    except Exception as e:
        write_to_logger(str(e), level='error')
        return "Error", 500

@app.route('/log', methods=['GET'])
def get_buffer_log():
    logs = get_logs()
    return jsonify(logs)

@app.route('/clear_log', methods=['GET'])
def clear_buffer_log():
    clear_logs()
    return "OK"

if __name__ == '__main__':
    logging.info('Starting server')
    app.run(host='0.0.0.0', port=5000)