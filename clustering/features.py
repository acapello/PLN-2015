# encoding: utf-8

from featureforge.feature import Feature


# class IsUsedToken(Feature):
#     """ Feature paramétrico que dice si un token es usado por el usuario
#         (en el vector de features, uno por cada token en el vocabulario)
#     """
#     def __init__(self, token):
#         self.token = token

#     def _evaluate(self, u):
#         assert isinstance(u, User)
#         return self.token in u.tokens

def bag_of_words(user):
    tokens = set()
    for tweet in user.tweets:
        tokens.update(tweet['tokens'])

    return tokens

def bag_of_hashtags(user):
    return user.hashtags

# def bag_of_bigrams(user):
#     return user.bigrams

# def user_name(user):


def user_location(user):
    return user.location

def user_description(user):
    return set(user.description)

# def user_is_verified(user):
#     return user.user_info['verified']

# def user_retweeted(user):
#     return 'el conjunto de usuario que este usuario retwiteo'
