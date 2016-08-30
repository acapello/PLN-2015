from clustering.user import User
from clustering.features import (bag_of_words, bag_of_hashtags,
                                 user_retweet_related)
# from clustering.features import (bag_of_bigrams, user_description,
#     user_location, user_name, user_is_verified, user_sum_favourites,
#     user_sum_retweet_count)
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from featureforge.vectorizer import Vectorizer
# from sklearn.preprocessing import StandardScaler


class Model(object):
    """docstring for Model"""

    def __init__(self, tweets):
        self.tweets = tweets
        self.users = users = dict()
        self.get_users()
        features = [
            bag_of_words,
            bag_of_hashtags,
            user_retweet_related(users),
            # user_description,
            # bag_of_bigrams,
            # user_location,
            # user_name,
            # user_is_verified,
            # user_sum_favourites,
            # user_sum_retweet_count,
            ]
        vect = Vectorizer(features)
        # scaler = StandardScaler(with_mean=False)
        clf = KMeans(init='k-means++', n_clusters=8)
        # self.pipeline = Pipeline(steps=[('vect', vect), ('scl', scaler), ('clf', clf)])
        self.pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])
        self.users_list = list(users.values())
        self.pipeline.fit(self.users_list)
        self.labels = self.pipeline.steps[1][1].labels_

    def get_users(self):
        users = self.users
        for tweet in self.tweets:
            if tweet['text'][:2] != 'RT':
                tweet['is_retweet'] = False
                self.add_user(tweet)
            else:
                # si es un retweet, tambien se agrega al usuario que creo el tweet.
                try:
                    # puede no estar este campo. En ese caso ignoramos el tweet.
                    source_tweet = tweet['retweeted_status']
                except KeyError:
                    continue

                source_tweet['is_retweet'] = False
                tweet['is_retweet'] = True
                tweet['text'] = None  # source_tweet['text']
                self.add_user(tweet)
                self.add_user(source_tweet)

                # actualizar atributos relacionados a retweet
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
