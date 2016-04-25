from clustering.features import User, IsUsedToken
from clustering.tokenizer.happyfuntokenizing import word_re, Tokenizer
from collections import Counter, defaultdict
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from featureforge.vectorizer import Vectorizer
from unicodedata import normalize



class Model(object):
    """docstring for Model"""

    def __init__(self, tweets):
        self.tweets = tweets
        users, voc = self.get_users_and_voc()
        self.users = users
        self.voc = voc

        features = [IsUsedToken(t) for t in voc]
        vect = Vectorizer(features)
        clf = KMeans(n_clusters=4)
        self.pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])
        self.pipeline.fit(users.values())


    def get_users_and_voc(self):
        """ Returns:
            users dict: (user_id: User object)
            vocabulary: set() [of tokens with count > 1]
        """
        users = dict()
        voc_counts = Counter()
        t = Tokenizer()
        normalize_text = lambda text: normalize('NFKD', text).encode('ASCII', 'ignore')
        for tweet in self.tweets:
            user_id = tweet['user']['id']
            text = normalize_text(tweet['text'])
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
