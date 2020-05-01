import sqlite3 as sql
import os
import json
conn = sql.connect("board_games" + os.path.sep + "content" + os.path.sep + "Database.db")

cursor = conn.cursor()
lobbies = dict()
free_lobby = 0
cursor.execute('CREATE TABLE IF NOT EXISTS lobbies('
               'id INTEGER PRIMARY KEY ON CONFLICT IGNORE,'
               'parameters TEXT)'
               )
conn.commit()
cursor.execute('CREATE TABLE IF NOT EXISTS players('
               'id INTEGER PRIMARY KEY,'
               'name TEXT, '
               'game INT)'
               )
conn.commit()

class Lobby:
    patch = ""

    # lobby_id, game, players, parameters = None
    def __init__(self, game, players, parameters):
        global free_lobby, cursor
        self.game = game
        self.players = players
        self.parameters = parameters
        self.lobby_id = free_lobby
        free_lobby += 1
        cursor.execute('INSERT INTO lobbies (id, parameters) VALUES (?, ?)', (self.lobby_id, str(self.game)))
        conn.commit()
        for player_id in self.players:
            cursor.execute('UPDATE players SET game = ? WHERE id = ?', (self.lobby_id, player_id))
        conn.commit()
        lobbies[self.lobby_id] = self
    def get_info(self):
        cursor.execute('SELECT * FROM lobbies WHERE id = ?', (str(self.lobby_id)))
        row = cursor.fetchone()
        return row[2]
    def update(self, new_game):
        self.game = new_game
        cursor.execute('UPDATE lobbies SET parameters = ? WHERE id = ?', (str(self.game), str(self.lobby_id)))
        conn.commit()

    '''
    def __del__(self):
        lobbies[self.lobby_id] = None
        cursor.execute('DELETE FROM lobbies WHERE id = ?', [self.lobby_id])
        conn.commit()
        cursor.execute('UPDATE players SET game = -1 WHERE id = ?', [self.lobby_id])
        conn.commit()
    '''
        # super(Lobby, self).__del__()





def get(id):
    return lobbies[id].get_info()
def update(id, game):
    lobbies[id].update(game)
def isExists(id):
    cursor.execute('SELECT * FROM lobbies WHERE id = ?', (str(id)))
    row = cursor.fetchone()
    if(row):
        return True
    else:
        return False

#update, check_is_exists
