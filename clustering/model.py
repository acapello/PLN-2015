from clustering.user import User
from clustering.features import bag_of_words, bag_of_hashtags, user_description, user_location
from collections import Counter, defaultdict
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
# from sklearn.preprocess import AlgunScaler
from featureforge.vectorizer import Vectorizer



class Model(object):
    """docstring for Model"""

    def __init__(self, tweets):
        self.tweets = tweets
        self.users = users = self.get_users()
        features = [bag_of_words, bag_of_hashtags, user_description, user_location]
        vect = Vectorizer(features)
        # scaler = AlgunScaler()
        clf = KMeans(n_clusters=3)
        # self.pipeline = Pipeline(steps=[('vect', vect), ('scl', scaler), ('clf', clf)])
        self.pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])
        self.pipeline.fit(users.values())


    def get_users(self):
        """ Returns:
            users dict: (user_id: User object)
            vocabulary: set() [of tokens with count > 1]
        """
        users = dict()
        for tweet in self.tweets:
            user_id = tweet['user']['id']
            if user_id in users.keys():
                u = users[user_id]
                u.update(tweet)
            else:
                u = User(tweet)
                users[user_id] = u

        return users