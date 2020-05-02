from board_games.DataStorage import DataStorage
import json


def player_action_module(json_str: str, lobby_id: int, player_id: int):
    dataStorage = DataStorage()
    dataStorage.initDB()
    action = json.loads(json_str)
    if not dataStorage.isExists(lobby_id):
        dataStorage.closeDB()
        return json.dumps({'status': 1, 'error': 'no lobby'})
    game = dataStorage.get_game(lobby_id)
    if str(player_id) not in game['players'].keys():
        dataStorage.closeDB()
        return json.dumps({'status': 1, 'error': 'no player in lobby'})
    game['events'].append(action)
    dataStorage.update(lobby_id, game)
    dataStorage.closeDB()
    return json.dumps({'status': 0})
