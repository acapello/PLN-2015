# encoding: utf-8
# Python 2.7 (porque se usa happyfuntokenizing)

import json # 'loads' used
from featureforge.feature import Feature
from happyfuntokenizing import word_re, Tokenizer
from collections import namedtuple, Counter, defaultdict
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from featureforge.vectorizer import Vectorizer
from wordcloud import WordCloud # https://github.com/amueller/word_cloud


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


def get_tweets():
    """ Obtener tweets (puros por el momento (sin RT))
        Devuelve una lista de diccionarios, donde cada diccionario es un tweet
        con toda su info. (entre ella el texto y el usuario)
    """
    f = open('tweets-balotaje1.txt', 'r')
    s = f.read()
    sp = s.split('\n')
    ts = [sp[i] for i in range(len(sp)) if i % 2 == 0 and sp[i] != '']
    tweets = []
    for t in ts:
        d = json.loads(t)
        a = d.get('text', '')
        if len(a) > 2 and a[:2] != 'RT':
            tweets.append(d)

    return tweets


def get_users_and_voc(tweets):
    """ Returns:
        users dict: (user_id: User object)
        vocabulary: set() [of tokens with count > 1]
    """
    users = dict()
    voc_counts = Counter()
    t = Tokenizer()
    for tweet in tweets:
        user_id = tweet['user']['id']
        text = tweet['text']
        tokens = t.tokenize(text)
        if user_id in users.keys():
            u = users[user_id]
            u.tokens.update(tokens)
            u.ntweets += 1
        else:
            u = User(id=user_id, tokens=set(tokens))
            users[user_id] = u

        voc_counts.update(tokens)

    voc = []
    for k, v in voc_counts.items():
        if v > 1:
            voc.append(k)

    return users, voc

def main():
    tweets = get_tweets()
    users, voc = get_users_and_voc(tweets)
    # return tweets, users, voc

    features = [IsUsedToken(t) for t in voc]
    vect = Vectorizer(features)
    clf = KMeans(n_clusters=4)
    pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])
    pipeline.fit(users.values())

    # print get_users_by_cluster(dict(users.items()[:50]), pipeline)

    return tweets, users, voc, pipeline


def execute():
    tweets, users, voc, pipeline = main()
    clf = get_users_by_cluster(users, pipeline)
    print_wordclouds_by_cluster(clf, users)

# AUX
# =============================================================================

def get_users_by_cluster(users, pipeline):
    """ Devuelve un defaultdict de listas donde los indices son los numeros de
        cluster, y el valor de cada uno es la lista de usuarios que están en ese
        cluster.
    """
    clf = defaultdict(list)
    for user_id, u in users.items():
        cluster_id = pipeline.predict([u])[0]
        clf[cluster_id].append(user_id)

    return clf

def print_wordclouds_by_cluster(clf, users):
    """ clf: la clasificación. (diccionario cluster_id:lista de user ids)
    """
    for cl_id, users_ids in clf.items():
        text = ""
        for u_id in users_ids:
            text += " ".join(users[u_id].tokens) + " "

        # Generate a word cloud image
        wordcloud = WordCloud().generate(text)

        # Display the generated image:
        # the matplotlib way:
        import matplotlib.pyplot as plt
        plt.imshow(wordcloud)
        plt.axis("off")

        # take relative word frequencies into account, lower max_font_size
        wordcloud = WordCloud(background_color="white", max_font_size=40, relative_scaling=.5).generate(text)
        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()



# =============================================================================

if __name__ == "__main__":
    execute()
    exit()

# EJECUTAR:
# ipython
# import work
# from work import *
# tweets, users, voc, pipeline = main()
# clf = get_users_by_cluster(users, pipeline)
# print_wordclouds_by_cluster(clf)

# Lo último sirve para ver la clasificación.
# Por ejemplo, para ver el texto de un user clasificado en el cluster 1 hacemos:
# users[clf[1][0]].tokens

# TIPOS
# tweets: lista de diccionarios (c/u tiene toda la info de 1 tweet)
# users: diccionario de {user id: objeto de clase User (el user con ese id)}
# voc: lista de tokens (strings)
# pipeline: Pipeline de scikit learn
# clf: diccionario de {cluster id: listas de ids de users (los clasificados en ese cluster)}