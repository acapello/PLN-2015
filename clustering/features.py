# encoding: utf-8

from featureforge.feature import Feature

class User:
    def __init__(self, id, tokens=set()):
        self.id = id
        self.tokens = set(tokens)
        self.ntweets = 1

class IsUsedToken(Feature):
    """ Feature paramétrico que dice si un token es usado por el usuario
        (en el vector de features, uno por cada token en el vocabulario)
    """
    def __init__(self, token):
        self.token = token

    def _evaluate(self, u):
        assert isinstance(u, User)
        return self.token in u.tokens