# encoding: utf-8

"""Train the model.

Usage:
  train.py -o <file>
  train.py -h | --help

Options:
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
# import sys
# sys.path.append("../")
# sys.path.append("../clustering")
from docopt import docopt
import pickle

from clustering.corpus.tweet_loader import get_tweets
from clustering.model import Model

if __name__ == '__main__':
    opts = docopt(__doc__)
    filename = opts['-o']

    # load the data
    # print("Loading corpus data...")
    tweets = get_tweets()
    model = Model(tweets)

    # save it
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
    exit()
