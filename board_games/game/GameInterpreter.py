import evalidate


def interprete(str, gamed: dict):
    bad = ['_', 'import', 'lambda']
    for i in bad:
        if i in str:
            raise Exception('bad source')
    exec(str, {}, {'game': gamed})