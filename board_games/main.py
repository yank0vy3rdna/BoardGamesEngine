from board_games.game import GameLoader
from board_games.DataStorage import *
from board_games.game.GameInterpreter import interprete

game_loader = GameLoader.GameLoader("board_games" + os.path.sep + "content" + os.path.sep + "game.zip", 28)
game = game_loader.get_game()


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
