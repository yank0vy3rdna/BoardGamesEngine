import base64

from flask import Flask, request

from board_games.RESTModules.closeLobby import closeLobby_module
from board_games.RESTModules.getLobbyData import getLobbyData_module
from board_games.RESTModules.createLobby import createLobby_module
from board_games.RESTModules.joinLobby import joinLobby_module
from board_games.RESTModules.player_action import player_action_module
from board_games.RESTModules.startGame import startGame_module

app = Flask(__name__)


@app.route('/board_games')
def get_page():
    with open("static/board_games/index.html") as f:
        return f.read()


@app.route('/board_games/getLobbyData', methods=['POST'])
def getLobbyData():
    lobbyid = request.form.get('lobbyid')
    return getLobbyData_module(lobbyid)


@app.route('/board_games/createLobby', methods=['POST'])
def createLobby():
    file = request.files['file']
    return createLobby_module(file)


@app.route('/board_games/player_action', methods=['POST'])
def player_action():
    lobby_id = request.form.get('lobby_id')
    player_id = request.form.get('player_id')
    content = request.form.get('json')
    return player_action_module(content, lobby_id, player_id)


@app.route('/board_games/joinLobby', methods=['POST'])
def joinLobby():
    lobby_id = request.form.get('lobby_id')
    player_id = request.form.get('player_id')
    nickname = request.form.get('nickname')
    return joinLobby_module(lobby_id, player_id, nickname)


@app.route('/board_games/closeLobby', methods=['POST'])
def closeLobby():
    lobby_id = request.form.get('lobby_id')
    return closeLobby_module(lobby_id)


@app.route('/board_games/startGame', methods=['POST'])
def startGame():
    lobby_id = request.form.get('lobby_id')
    player_id = request.form.get('player_id')
    return startGame_module(lobby_id, player_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
