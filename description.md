# Boardscript

Programming language for describing board games.


## Packaging
 
zip archive with folders structure:

```
Game.zip/
- assets/
- - card1/
- - - config.json
- - - face.png
- - - back.png
- - flamethrower/
- - - config.json
- - - 1.png
- - - 4.png
- - map1/
- - - config.json
- - - v.png
- player_types/
- - nechto/
- - - config.json
- - human/
- - - config.json
- game.json
- main.py
```

## Config file of asset(config.json)
Contains:
- name(str)
- type(str): "map", "card", "dice"

Optional:
- face image file name(str): required for map and card
- back image file name(str): required for card
- anything u want to store there for your logic

Example:
```
{
    "name": "ExampleNameOfAsset",
    "type": "card",
    "in_start_hand": true,
    "face_image": "1.png",
    "back_image": "4.png"
}
```

## Config file of game
Contains:
- name(str)
