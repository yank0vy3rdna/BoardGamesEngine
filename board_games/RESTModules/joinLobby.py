import json

from board_games.DataStorage import DataStorage


def joinLobby_module(lobby_id: int, user_id: int, username: str):
    dataStorage = DataStorage()
    dataStorage.initDB()
    game = dataStorage.get_game(lobby_id)
    user_id_search = None
    for key, value in game['players'].items():
        if value['nickname'] == username:
            user_id_search = key
            break
    if user_id_search is None:
        if len(game['players'].keys()) >= game['max_players_count']:
            dataStorage.closeDB()
            return json.dumps({'status': 2})
        game_master = 0
        if len(game['players'].keys()) == 0:
            game_master = 1
        game['players'].update({user_id: {
            'player_type': '-',
            'id': user_id,
            'nickname': username,
            'player_queue': [],
            'is_game_master': game_master
        }})
        dataStorage.update(lobby_id, game)
        dataStorage.closeDB()
        return json.dumps(game)
    if user_id_search != user_id:
        dataStorage.closeDB()
        return json.dumps({'status': 1, 'error': 'nickname is already used'})
    if user_id_search == user_id:
        game['players'].update({user_id: {
                    'player_type': '-',
                    'id': user_id,
                    'nickname': username,
                    'is_game_master': 0
                }})
        dataStorage.update(lobby_id, game)
        dataStorage.closeDB()
        return json.dumps(game)