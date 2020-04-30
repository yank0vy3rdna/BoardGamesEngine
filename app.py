from flask import Flask

app = Flask(__name__)


@app.route('/board_games')
def hello_world():
    with open("static/index.html") as f:
        return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
