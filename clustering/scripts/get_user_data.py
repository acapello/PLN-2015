# encoding: utf-8

"""Evaulate a model.

Usage:
  get_user_tweets.py -i <file> -u <user_id>
  get_user_tweets.py -h | --help

Options:
  -i <file>     Model file.
  -u <user_id>  User id number.
  -h --help     Show this screen.
"""

from docopt import docopt
import pickle

if __name__ == '__main__':
    opts = docopt(__doc__)

    filename = opts['-i']
    user_id = int(opts['-u'])

    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    u = model.users[user_id]
    cluster = model.pipeline.predict([u])[0]
    name = u.tweets[0]['raw_tweet']['user']['name']
    description = u.tweets[0]['raw_tweet']['user']['description']
    print("Usuario: {:<12}    Nombre: {:<12}".format(u.screen_name, name))
    print("Seguidores: {:<12} Seguidos: {:<12}".format(u.followers_count, u.friends_count))
    print("Descripción: {:<12}".format(description))
    print("Clasificado en cluster: {:<12}".format(cluster))
    print("Retwitteo a: {:<12}".format(" ".join(map(str, u.retweeted_to))))
    print("=" * 36 + " Tweets " + "=" * 36 + "\n")
    for tweet_struct in u.tweets:
        text = tweet_struct['raw_tweet']['text']
        if text is None:
            continue
        for text in text.split("\n"):
            print("    {:<12}".format(str(text)))
        print()
    print("=" * 80)
