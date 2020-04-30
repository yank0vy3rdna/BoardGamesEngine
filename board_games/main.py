from board_games.game import GameLoader, GameInterpreter
game_loader = GameLoader.GameLoader("/home/yank0vy3rdna/projects/AllSite/board_games/content/game.zip")
game = game_loader.get_game()
GameInterpreter.GameInterpreter().interprete("a = 0", game)

print(game)
