from flask import Flask, jsonify, request
import socket
import datetime 

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'hostname': socket.gethostname(),
        'message': 'Hello, World4!'
        })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")