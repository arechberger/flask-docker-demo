import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! This is version: 0.0.3"


@app.route("/hostname")
def hostname():
    HOSTNAME = os.getenv("HOSTNAME", "unknown")
    return f"You are on host {HOSTNAME}"
