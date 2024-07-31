
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Return a plain text message
    return 'Hello from the server! This is a plain text message.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
