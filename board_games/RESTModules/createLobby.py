import time
import os
import json
from board_games.DataStorage import DataStorage
from board_games.game.GameLoader import GameLoader


def createLobby_module(file):
    lobby_id = int(time.time())
    path = 'board_games' + os.path.sep + 'content' + os.path.sep + 'lobbies' + os.path.sep + str(
        lobby_id) + os.path.sep + 'file.zip'
    file.save(path)
    dataStorage = DataStorage()
    dataStorage.initDB()
    try:
        game_loader = GameLoader(file, lobby_id)
        dataStorage.createLobby(game_loader.get_game(), lobby_id)
        dataStorage.closeDB()
        return json.dumps({'lobby_id': lobby_id})
    except Exception as e:
        return json.dumps({'status': 1, 'error': str(e)})
