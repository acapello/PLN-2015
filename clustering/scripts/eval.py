# encoding: utf-8

"""Evaulate a model.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Model file.
  -h --help     Show this screen.
"""

# import sys
# sys.path.append("../")
# sys.path.append("../clustering")

from docopt import docopt
import pickle
from collections import defaultdict
from wordcloud import WordCloud # https://github.com/amueller/word_cloud
import matplotlib.pyplot as plt


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
            tokens = set()
            for tweet in users[u_id].tweets:
                tokens.update(tweet['tokens'])

            text += " ".join(tokens) + " "

        # Generate a word cloud image, take relative word frequencies into account, lower max_font_size
        wordcloud = WordCloud(background_color="white", max_font_size=40, relative_scaling=.5).generate(text)
        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    # print("\nLoading the model...")
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()
    # print("Model type: %s" % type(model))

    # evaluate
    clf = get_users_by_cluster(model.users, model.pipeline)
    print_wordclouds_by_cluster(clf, model.users)
