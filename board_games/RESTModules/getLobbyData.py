from board_games.DataStorage import *


def getLobbyData_module(lobby_id: int):
    if isExists(lobby_id):
        return get(lobby_id)
    else:
        return "{'status': 1}"
