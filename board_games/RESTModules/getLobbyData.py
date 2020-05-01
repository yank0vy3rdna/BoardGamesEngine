from board_games.DataStorage import DataStorage


def getLobbyData_module(lobby_id: int):
    dataStorage = DataStorage()
    dataStorage.initDB()
    if dataStorage.isExists(lobby_id):
        data = dataStorage.get_info(lobby_id)
        dataStorage.closeDB()
        return data
    else:
        dataStorage.closeDB()
        return "{'status': 1}"
