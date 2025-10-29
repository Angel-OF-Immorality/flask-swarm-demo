from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

visit_count = 0

@app.route('/')
def hello():
    global visit_count
    visit_count += 1
    hostname = socket.gethostname()
    return jsonify({
        'message': 'Hello from Docker Swarm v2 - Rolling Updates!',
        'hostname': hostname,
        'visit_count': visit_count,
        'version': os.getenv('APP_VERSION', '2.0')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
