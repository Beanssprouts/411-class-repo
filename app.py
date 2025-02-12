from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {"response": "Hello, World!", "status": 200}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Default to 5000 if PORT not set
    app.run(host='0.0.0.0', port=port)