from zipfile import ZipFile
import os
import json
import base64


class GameLoader:
    path = None
    game = {'assets': {}, 'player_types': {}, 'script': ''}
    is_path_true = False

    def get_game(self):
        return self.game

    def extract_zip(self, archive_file: str):
        if self.is_path_true:
            with ZipFile(archive_file, "r") as zipObj:
                zipObj.extractall(self.path)

    def get_assets_dirs(self):
        return [self.path + os.path.sep + 'assets' + os.path.sep + i
                for i in os.listdir(self.path + os.path.sep + 'assets')]

    def get_playertypes_path(self):
        return [self.path + os.path.sep + 'player_types' + os.path.sep + i
                for i in os.listdir(self.path + os.path.sep + 'player_types')]

    def parse_asset(self, path):
        asset = json.load(open(path + os.path.sep + 'config.json'))
        asset['__path__'] = path
        if asset['name'] in self.game['assets'].keys():
            raise Exception("Name conflict in assets")
        if 'face_image' in asset:
            if not os.path.exists(path + os.path.sep + asset['face_image']):
                raise Exception("Face image not found")
            asset['face_base64'] = base64.b64encode(
                open(path + os.path.sep + asset['face_image'], 'rb').read()).decode(encoding='ascii')
        if 'back_image' in asset:
            if not os.path.exists(path + os.path.sep + asset['back_image']):
                raise Exception("Back image not found")
            asset['back_base64'] = base64.b64encode(
                open(path + os.path.sep + asset['back_image'], 'rb').read()).decode(encoding='ascii')
        self.game['assets'][asset['name']] = asset

    def parse_playertype(self, path):
        playertype = json.load(open(path + os.path.sep + 'config.json'))
        playertype['__path__'] = path
        if playertype['name'] in self.game['player_types'].keys():
            raise Exception("Name conflict in player_types")
        self.game['player_types'][playertype['name']] = playertype

    def get_script(self):
        self.game['script'] = open(self.path + os.path.sep + "main.py").read()

    def __init__(self, archive_file: str, lobby_id: int):
        self.is_path_true = os.path.exists(archive_file) \
                            and len(archive_file.split('.')) > 1 \
                            and archive_file.split('.')[1] == 'zip'
        if not self.is_path_true:
            raise Exception("Path to zip file broken")
        self.path = 'board_games' + os.path.sep + 'content' + os.path.sep + 'lobbies' + os.path.sep + str(lobby_id)
        self.lobby_id = lobby_id

        self.extract_zip(archive_file)

        self.path = self.path + os.path.sep + 'game'

        assets_path = self.get_assets_dirs()

        playertypes_path = self.get_playertypes_path()

        self.game.update(json.load(open(self.path+os.path.sep+'game.json')))

        self.game['players'] = {}

        for i in assets_path:
            self.parse_asset(i)

        for i in playertypes_path:
            self.parse_playertype(i)

        self.get_script()
