from board_games.game import GameLoader, GameInterpreter
from board_games.DataStorage import *

game_loader = GameLoader.GameLoader("/home/yank0vy3rdna/projects/AllSite/board_games/content/game.zip")
game = game_loader.get_game()
game['name']='prikol'
print(game)
Lobby(game, [54], {'max_players_count': 4})

# GameInterpreter.GameInterpreter().interprete("a = 0", game)

