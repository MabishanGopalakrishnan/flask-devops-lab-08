from flask import Flask
import random

app = Flask(__name__)

QUOTES = [
    "Ship small, ship often.",
    "Automation beats manual work.",
    "Fail fast, recover faster.",
    "Tests are your safety net.",
    "CI/CD keeps you moving forward.",
]


@app.route("/")
def hello():
    return "Hello, DevOps World!"


@app.route("/motivator")
def motivator():
    return random.choice(QUOTES)


if __name__ == "__main__":
    app.run()
