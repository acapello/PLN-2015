# encoding: utf-8

"""Print user data, like Username and tweets.

Usage:
  print_user_data.py -i <file> -u <user_id>
  print_user_data.py -h | --help

Options:
  -i <file>     Model file.
  -u <user_id>  User id number.
  -h --help     Show this screen.
"""

from docopt import docopt
import pickle


def print_user_data(u):
    name = u.tweets[0]['raw_tweet']['user']['name']
    print("Usuario: {:<12}    Nombre: {:<12}    Id: {:<12}".format(u.screen_name, name, u.id))
    print("Seguidores: {:<12} Seguidos: {:<12}".format(u.followers_count, u.friends_count))
    description = str(u.tweets[0]['raw_tweet']['user']['description'])
    print("Descripción: {:<12}".format(description))

    print("Retwitteado por: {:<12}".format(" ".join(map(str, u.retweeted_by))))
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


if __name__ == '__main__':
    opts = docopt(__doc__)

    filename = opts['-i']
    user_id = int(opts['-u'])

    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    user = model.users[user_id]
    print_user_data(user)
    cluster = model.pipeline.predict([user])[0]
    print("Clasificado en cluster: {:<12}".format(cluster))
