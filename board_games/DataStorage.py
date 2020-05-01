import sqlite3 as sql
import os

conn = sql.connect("content" + os.path.sep + "Database.db")

cursor = conn.cursor()
lobbies = dict()
free_lobby = 0
cursor.execute('CREATE TABLE IF NOT EXISTS lobbies('
               'id INTEGER PRIMARY KEY,'
               'name TEXT)'
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
        cursor.execute('INSERT INTO lobbies (id, name) VALUES (?, ?)', (self.lobby_id, self.game['name']))
        conn.commit()
        cursor.execute('UPDATE players SET game = ? WHERE id IN ?', (self.lobby_id, self.players))
        conn.commit()
        lobbies[self.lobby_id] = self

    def __del__(self):
        lobbies[self.lobby_id] = None
        cursor.execute('DELETE FROM lobbies WHERE id = ?', [self.lobby_id])
        conn.commit()
        cursor.execute('UPDATE players SET game = -1 WHERE id = ?', [self.lobby_id])
        conn.commit()
        # super(Lobby, self).__del__()
