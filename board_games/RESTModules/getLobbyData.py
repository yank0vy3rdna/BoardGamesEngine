from board_games.DataStorage import DataStorage
import json


def getLobbyData_module(lobby_id: int):
    dataStorage = DataStorage()
    dataStorage.initDB()
    if dataStorage.isExists(lobby_id):
        data = dataStorage.get_game(lobby_id)
        dataStorage.closeDB()
        return json.dumps(data)
    else:
        dataStorage.closeDB()
        return '{"status": 1}'
