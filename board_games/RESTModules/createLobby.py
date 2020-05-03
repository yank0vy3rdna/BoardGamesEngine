import time
import os
import json
from board_games.DataStorage import DataStorage
from board_games.game.GameLoader import GameLoader


def createLobby_module(file):
    lobby_id = int(time.time())  # id лобби - текущий юникстайм

    path = 'board_games' + os.path.sep + 'content' + os.path.sep + 'lobbies' + os.path.sep + str(
        lobby_id) # Файл из запроса сохраняется в папку с id лобби
    if not os.path.exists(path):
        os.makedirs(path)
    path += os.path.sep + 'file.zip'
    file.save(path)

    dataStorage = DataStorage()
    dataStorage.initDB()
    try:
        game_loader = GameLoader(path, lobby_id)  # Чтение zip архива
        game = game_loader.get_game()

        # game['players'].update(  # В лобби сначала только создатель
        #     {
        #         user_id: {
        #             'player_type': '-',
        #             'id': user_id,
        #             'nickname': nickname,
        #             'is_game_master': 1
        #         }
        #     }
        # )
        dataStorage.createLobby(game, lobby_id)  # Записываем данные о лобби в бд
        dataStorage.closeDB()
        return json.dumps({'lobby_id': lobby_id})
    except Exception as e:
        return json.dumps({'status': 1, 'error': str(e)})
