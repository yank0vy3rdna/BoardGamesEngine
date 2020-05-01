from flask import Flask
from board_games.RESTModules.getLobbyData import getLobbyData_module

app = Flask(__name__)


@app.route('/board_games')
def get_page():
    with open("static/index.html") as f:
        return f.read()


@app.route('/board_games/getLobbyData?lobbyid=123')
def getLobbyData(lobbyid: int):
    return getLobbyData_module(lobbyid)


# @app.route('/board_games/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
