from board_games.game import GameLoader
from board_games.DataStorage import *
from board_games.game.GameInterpreter import interprete

game_loader = GameLoader.GameLoader("board_games" + os.path.sep + "content" + os.path.sep + "game.zip", 28)
game = game_loader.get_game()
print(json.dumps(game))
game['players'] = {
    132324: {
        'player_type': 'Human',
        'id': 132324,
        'nickname': 'motherfucker',
        'coins_count': 3
    }
}
game['scene'] = {
    "map": {
        "card1": {
            "type": "Flamethrower",
            "image": "face_image",
            'whereis': 'koloda1'
        },
        "koloda1":{
            'type': 'koloda',
            'whereis':{
                'x':360,
                'y': 200
            }
        },
        "koloda2":{
            'type': 'koloda',
            'whereis': '132324'
        }
    }
}
src = """game.update({"ghafg": "asd"})"""

interprete(src, game)

from board_games.DataStorage import DataStorage
dataStorage = DataStorage()
dataStorage.initDB()
lobby_id = dataStorage.createLobby(game, int(time.time()))
a = dataStorage.get_game(lobby_id)
print(dataStorage.isExists(lobby_id))
print(dataStorage.isExists(-1))
dataStorage.closeDB()
import json
print(json.dumps(game))



# GameInterpreter.GameInterpreter().interprete("a = 0", game)
