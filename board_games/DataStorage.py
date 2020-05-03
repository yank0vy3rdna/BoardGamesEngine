import sqlite3 as sql
import os
import time
import json


class DataStorage:

    def initDB(self):
        self.conn = sql.connect("board_games" + os.path.sep + "content" + os.path.sep + "Database.db")

    def closeDB(self):
        self.conn.close()

    # lobby_id, game, players, parameters = None
    def createLobby(self, game, lobby_id: int) -> int:
        print(json.dumps(game))
        self.conn.cursor().execute('INSERT INTO main.lobbies (id, game) VALUES (?, ?)',
                                   (str(lobby_id), json.dumps(game)))
        self.conn.commit()
        return lobby_id

    def get_game(self, lobby_id: int):
        cursor = self.conn.cursor()
        cursor.execute('SELECT game FROM main.lobbies WHERE id = ?', (str(lobby_id),))
        row = cursor.fetchone()
        return json.loads(row[0])

    def update(self, lobby_id: int, new_game):
        self.conn.cursor().execute('UPDATE main.lobbies SET game = ? WHERE id = ?', (json.dumps(new_game), str(lobby_id)))
        self.conn.commit()

    def delete(self, lobby_id: int):
        self.conn.cursor().execute('DELETE main.lobbies WHERE id = ?', (str(lobby_id),))
        self.conn.commit()

    def isExists(self, lobby_id: int):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id FROM main.lobbies WHERE id = ?', (str(lobby_id),))
        row = cursor.fetchone()
        if row:
            return True
        else:
            return False
