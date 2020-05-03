def createKoloda(game, koloda_name, whereis: str, is_hand: bool):
    if whereis in game['players'].keys() or whereis in game['scene'] or whereis == 'map':
        game['scene'].update({koloda_name: {'type': 'koloda', 'queue': [], 'whereis': whereis, 'ishand': is_hand}})


def createCard(asset, game, cardname, whereis, isFace):
    image = 'back_base64'
    if isFace:
        image = 'face_base64'
    if whereis == 'map':
        if cardname not in game['scene'].keys() and cardname not in game['scene']['map_queue']:
            game['scene'].update({cardname: {'type': asset, 'image': image, 'whereis': whereis}})
            game['scene']['map_queue'].append(cardname)
    if whereis in game['players'].keys():
        if cardname not in game['scene'].keys() and cardname not in game['players'][whereis]['player_queue']:
            game['players'][whereis]['player_queue'].append(cardname)
            game['scene'].update({cardname: {'type': asset, 'image': image, 'whereis': whereis}})
    if whereis in game['scene']:
        if cardname not in game['scene'] and cardname not in game['scene'][whereis]['queue']:
            game['scene'][whereis]['queue'].append(cardname)
            game['scene'].update({cardname: {'type': asset, 'image': image, 'whereis': whereis}})


def changeFace(game, cardname):
    if cardname in game['scene']:
        if 'image' in game['scene'][cardname].keys():
            if game['scene'][cardname]['image'] == 'back_base64':
                game['scene'][cardname]['image'] = 'front_base64'
            if game['scene'][cardname]['image'] == 'front_base64':
                game['scene'][cardname]['image'] = 'back_base64'


def moveCard(game, cardname, whereis):
    oldwhereis = game['scene'][cardname]['whereis']
    if cardname in game['scene']:
        if whereis == 'map':
            if oldwhereis in game['players'].keys():
                if cardname in game['players'][oldwhereis]['player_queue']:
                    game['players'][oldwhereis]['player_queue'].remove(cardname)
                    game['scene']['map_queue'].append(cardname)
                    game['scene'][cardname]['whereis'] = whereis
            if oldwhereis in game['scene']:
                if cardname in game['scene'][oldwhereis]['queue']:
                    game['scene'][oldwhereis]['queue'].remove(cardname)
                    game['scene']['map_queue'].append(cardname)
                    game['scene'][cardname]['whereis'] = whereis
        if whereis in game['players'].keys():
            if oldwhereis == 'map':
                if cardname in game['scene']['map_queue']:
                    game['scene'][oldwhereis]['map_queue'].remove(cardname)
                    game['players'][whereis]['player_queue'].append(cardname)
                    game['scene'][cardname]['whereis'] = whereis
            if oldwhereis in game['players'].keys():
                if cardname in game['players'][oldwhereis]['player_queue']:
                    game['players'][oldwhereis]['player_queue'].remove(cardname)
                    game['players'][whereis]['player_queue'].append(cardname)
                    game['scene'][cardname]['whereis'] = whereis
            if oldwhereis in game['scene'].keys():
                if cardname in game['scene'][oldwhereis]['queue']:
                    game['scene'][oldwhereis]['queue'].remove(cardname)
                    game['players'][whereis]['player_queue'].append(cardname)
                    game['scene'][cardname]['whereis'] = whereis
        if whereis in game['scene'].keys():
            if game['scene'][whereis]['type'] == 'koloda':
                if oldwhereis == 'map':
                    if cardname in game['scene']['map_queue']:
                        game['scene'][oldwhereis]['map_queue'].remove(cardname)
                        game['scene'][whereis]['queue'].append(cardname)
                        game['scene'][cardname]['whereis'] = whereis
                if oldwhereis in game['players'].keys():
                    if cardname in game['players'][oldwhereis]['player_queue']:
                        game['players'][oldwhereis]['player_queue'].remove(cardname)
                        game['scene'][whereis]['queue'].append(cardname)
                        game['scene'][cardname]['whereis'] = whereis
                if oldwhereis in game['scene'].keys():
                    if cardname in game['scene'][oldwhereis]['queue']:
                        game['scene'][oldwhereis]['queue'].remove(cardname)
                        game['scene'][whereis]['queue'].append(cardname)
                        game['scene'][cardname]['whereis'] = whereis


def pullKoloda(game, kolodaName, whereis):
    if kolodaName in game['scene']:
        if game['scene'][kolodaName]['type'] == 'koloda':
            if len(game['scene'][kolodaName]['queue']) > 0:
                card = game['scene'][kolodaName]['queue'][-1]
                game['scene'][kolodaName]['queue'].remove(card)
                if whereis == 'map':
                    game['scene']['map_queue'].append(card)
                if whereis in game['players'].keys():
                    game['players']['player_queue'].append(card)
                if whereis in game['scene'].keys():
                    game['scene'][whereis]['queue'].append(card)


def interprete(str, gamed: dict):
    bad = ['__', 'import', 'lambda']
    for i in bad:
        if i in str:
            raise Exception('bad source')
    exec(str, {}, {'game': gamed, 'createCard': createCard, 'pullKoloda': pullKoloda, 'moveCard': moveCard, 'changeFace': changeFace, 'createKoloda': createKoloda})
