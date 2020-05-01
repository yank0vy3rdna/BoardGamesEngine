from board_games.game import GameLoader, GameInterpreter
from board_games.DataStorage import *

game_loader = GameLoader.GameLoader("board_games" + os.path.sep + "content" + os.path.sep + "game.zip", 28)
game = game_loader.get_game()
game['name'] = 'prikol'
game['players'] = {
    132324: {
        'player_type': 'Human',
        'id': 132324,
        'nickname': 'motherfucker',
        'coins_count': 3
    }
}
game['scene']={
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
from board_games.DataStorage import DataStorage
dataStorage = DataStorage()
dataStorage.initDB()
lobby_id = dataStorage.createLobby(game)
a = dataStorage.get_info(lobby_id)
print(dataStorage.isExists(lobby_id))
print(dataStorage.isExists(-1))
dataStorage.closeDB()
import json
print(json.dumps(game))



# GameInterpreter.GameInterpreter().interprete("a = 0", game)
