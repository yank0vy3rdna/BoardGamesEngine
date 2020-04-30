from ast import literal_eval


class GameInterpreter:
    def __init__(self):
        pass

    def interprete(self, str, objectmodel):
        literal_eval(str)
