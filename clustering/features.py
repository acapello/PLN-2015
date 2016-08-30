# encoding: utf-8

from featureforge.feature import Feature


def bag_of_words(user):
    tokens = set()
    for tweet in user.tweets:
        tokens.update(tweet['tokens'])

    return tokens


def bag_of_bigrams(user):
    bigrams = set()
    for tweet in user.tweets:
        last = 'BOS'
        for token in tweet['tokens']:
            bigrams.add((last, token))
            last = token

    return bigrams


def bag_of_hashtags(user):
    return user.hashtags


def user_description(user):
    return set(user.description)


def user_location(user):
    return user.location


def user_name(user):
    return user.name


def user_is_verified(user):
    return user.verified


def user_sum_favourites(user):
    return user.sum_favourites


def user_sum_retweet_count(user):
    return user.sum_retweet_count


class user_retweet_related(Feature):

    def __init__(self, users_dict):
        self.users_dict = users_dict

    def _evaluate(self, user):
        users_related = set()
        for u_id in user.retweeted_by + user.retweeted_to:
            u = self.users_dict[u_id]
            users_related.add(u.id_str)
        users_related.add(user.id_str)

        return users_related
