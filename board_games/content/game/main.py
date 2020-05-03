for i in game['players'].keys():
    createKoloda(game, 'koloda_' + i, i, False)
    for asset in game['assets']:
        if game['assets'][asset]['type'] == 'card':
            createCard(asset, game, asset+'_'+i, 'koloda_'+i, False)