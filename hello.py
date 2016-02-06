"""Simple start up guide for printing out hello world."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Response with hello world only."""
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
