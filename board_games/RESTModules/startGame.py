import json

from board_games.DataStorage import DataStorage
from board_games.game.GameInterpreter import interprete


def startGame_module(lobby_id: int, player_id):
    dataStorage = DataStorage()
    dataStorage.initDB()
    try:
        game = dataStorage.get_game(lobby_id)
        if game['players'][player_id]['is_game_master'] == 1 and game['min_players_count'] <= len(game['players'].keys()):
            game['started']=1
            game['scene'] = {'map_queue': []}
            interprete(game['__main__'], game)
            dataStorage.update(lobby_id, game)
            dataStorage.closeDB()
            return json.dumps({'status': 0, 'msg': 'game started'})
        else:
            dataStorage.closeDB()
            return json.dumps({'status': 2})
    except Exception as e:
        dataStorage.closeDB()
        return json.dumps({'status': 1})
