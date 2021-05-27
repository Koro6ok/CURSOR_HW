from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Your name!"


@app.route('/hello')
def hello():
    return 'My name!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)