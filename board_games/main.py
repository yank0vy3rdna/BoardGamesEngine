from board_games.game import GameLoader, GameInterpreter
from board_games.DataStorage import *

game_loader = GameLoader.GameLoader("board_games" + os.path.sep + "content" + os.path.sep + "game.zip")
game = game_loader.get_game()
game['name'] = 'prikol'
print(game)
Lobby(game, [54], {'max_players_count': 4})

# GameInterpreter.GameInterpreter().interprete("a = 0", game)
