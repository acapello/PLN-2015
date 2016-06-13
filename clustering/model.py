from clustering.user import User
from clustering.features import (bag_of_words, bag_of_bigrams, bag_of_hashtags,
    user_description, user_location, user_name, user_is_verified,
    user_sum_favourites, user_sum_retweet_count, user_retweet_related)
from collections import Counter, defaultdict
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from featureforge.vectorizer import Vectorizer



class Model(object):
    """docstring for Model"""

    def __init__(self, tweets):
        self.tweets = tweets
        self.users = users = dict()
        self.get_users()
        features = [bag_of_words,
                    bag_of_hashtags,
                    user_description,
                    user_retweet_related(users),
                    # bag_of_bigrams,
                    # user_location,
                    # user_name,
                    # user_is_verified
                    # user_sum_favourites
                    # user_sum_retweet_count
        ]
        vect = Vectorizer(features)
        # scaler = StandardScaler(with_mean=False)
        clf = KMeans(n_clusters=3)
        # self.pipeline = Pipeline(steps=[('vect', vect), ('scl', scaler), ('clf', clf)])
        self.pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])
        self.users_list = list(users.values())
        self.pipeline.fit(self.users_list)


    def get_users(self):
        """ Returns:
            users dict: (user_id: User object)
        """
        users = self.users
        for tweet in self.tweets:
            if tweet['text'][:2] != 'RT':
                self.add_user(tweet)
            else:
                # si es un retweet, tambien agrego al usuario que creo el tweet
                # print(tweet)
                try:
                    # debería estar siempre este campo.. pero a veces no está
                    source_tweet = tweet['retweeted_status']
                except KeyError:
                    continue

                # el texto del tweet es el mismo que el de origen..
                # (sin rt y el nombre de usuario...) sino hay palabras incompletas.
                tweet['text'] = source_tweet['text']
                self.add_user(tweet)
                self.add_user(source_tweet)

                # update retweeted attributes
                uid = tweet['user']['id']
                retweeted_uid = source_tweet['user']['id']
                users[uid].retweeted_to.append(retweeted_uid)
                users[retweeted_uid].retweeted_by.append(uid)


    def add_user(self, tweet):
        users = self.users
        user_id = tweet['user']['id']
        if user_id in users.keys():
            u = users[user_id]
            u.update(tweet)
        else:
            u = User(tweet)
            users[user_id] = u

        return users