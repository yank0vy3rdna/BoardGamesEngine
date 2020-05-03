import json
import os

from board_games.DataStorage import DataStorage


def closeLobby_module(lobby_id: int):
    dataStorage = DataStorage()
    dataStorage.initDB()
    if dataStorage.isExists(lobby_id):
        dataStorage.delete(lobby_id)
        os.rmdir('board_games'+os.path.sep+'content'+os.path.sep+'lobbies'+os.path.sep+str(lobby_id))
    else:
        dataStorage.closeDB()
        return json.dumps({'status': 1})
    dataStorage.closeDB()
    return json.dumps({'status': 0})