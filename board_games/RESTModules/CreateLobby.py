from flask import Flask, request
import os
import base64
import json
from werkzeug.utils import secure_filename
import board_games.DataStorage as ds
import board_games.game.GameLoader as gl
app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
@app.route('/board_games/CreateLobby', methods=['POST'])
def createLobby():
    file = base64.b64decode(request.files['file']).decode("UTF-8")
    filename = secure_filename(file.filename)
    lobby_id = ds.free_lobby
    lobby = gl.GameLoader(file, lobby_id)
    ds.Lobby(lobby.game, [], [])
    path = "board_games" + os.path.sep + "lobbies" + os.path.sep + "lobby_" + lobby_id + os.path.sep + "file.zip"
    file.save(os.path.join(path))
    return json.encoder(lobby_id)

