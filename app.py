from flask import Flask, request
from board_games.RESTModules.getLobbyData import getLobbyData_module

app = Flask(__name__)


@app.route('/board_games')
def get_page():
    with open("static/board_games/index.html") as f:
        return f.read()


@app.route('/board_games/getLobbyData')
def getLobbyData():
    lobbyid = request.args.get('lobbyid')
    return getLobbyData_module(lobbyid)


# @app.route('/board_games/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
