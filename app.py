from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "response": "Hello, World!",
        "status": 200
    })

@app.route('/repeat')
def repeat():
    input_text = request.args.get('input', '')
    return jsonify({
        "body": input_text,
        "status": 200
    })

@app.route('/health')
@app.route('/healthcheck')
def health():
    return jsonify({
        "body": "OK",
        "status": 200
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)