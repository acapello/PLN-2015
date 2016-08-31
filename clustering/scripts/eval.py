# encoding: utf-8

"""Evaulate a model.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Model file.
  -h --help     Show this screen.
"""

from docopt import docopt
import pickle
from collections import defaultdict, Counter
from wordcloud import WordCloud  # https://github.com/amueller/word_cloud
import matplotlib.pyplot as plt
import os
import shutil  # for creating / removing directory

from clustering.data import hs_m, hs_s  # , hs_o


def get_users_by_cluster(model):
    # No usada, solo por si se quiere usar una clasificación simple (no ordenada)
    clf = defaultdict(list)

    kmeans = model.pipeline.steps[1][1]
    for i, u in enumerate(model.users_list):
        clf[kmeans.labels_[i]].append(u)

    return clf


def plot_wordclouds_by_cluster(clf):
    """ clf: la clasificación. (diccionario cluster_id:lista de user ids)

    """
    # reset directory for wordclouds
    dir = 'clustering/wordclouds'
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    print('=' * 80)
    print("Clasificación del algoritmo K-Means:")
    # print("{:>18}   {:<22}".format('Id Cluster', 'Número de Usuarios'))
    for cl_id, users in clf.items():
        text = ""
        c = Counter()
        c_users = Counter()
        c_users_rt = 0
        for u in users:
            tokens = u.user_tokens()
            if u.retweets_count >= u.tweets_count:
                c_users_rt += 1
            c.update(tokens)
            c_users.update(set(tokens))
            text += " ".join(tokens) + " "

        # Generate a word cloud image, take relative word frequencies into account, lower max_font_size
        # can add max_font_size=40, relative_scaling=.5
        wordcloud = WordCloud(width=800, height=400, background_color="white", relative_scaling=.2).generate(text)
        plt.figure(figsize=(20, 10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=1)
        # plt.show()
        plt.savefig("clustering/wordclouds/wc_cluster_{}".format(cl_id))
        print("Cluster {}: {} usuarios - {} retwitteros".format(cl_id, len(users), c_users_rt))
        n = 20
        print('\t{} tokens más usados:    {:<10} {:<10}'.format(n, "repeticiones", "usuarios que lo usaron"))
        for token, count in c.most_common(n):
            print("\t{:>22}   {:<10}   {:<10}".format(token, count, c_users[token]))
        print('-' * 80)


def plot_wordclouds_of_preferences(users_list):
    l0, l1, l2, l3 = [], [], [], []
    count_m, count_s, count_o1, count_o2 = 0, 0, 0, 0
    for u in users_list:
        hs = set(u.hashtags)
        # macristas
        i_m = len(hs.intersection(hs_m))
        i_s = len(hs.intersection(hs_s))
        if i_m != 0 and i_s == 0:
            l0 += u.user_tokens()
            count_m += 1
        # sciolistas
        elif i_s != 0 and i_m == 0:
            l1 += u.user_tokens()
            count_s += 1
        # otros
        elif i_m != 0 and i_s != 0:
            l2 += u.user_tokens()
            count_o1 += 1
        else:
            l3 += u.user_tokens()
            count_o2 += 1

    l = [l0, l1, l2, l3]
    for i in range(4):
        text = " ".join(l[i])
        wordcloud = WordCloud(width=800, height=400, background_color="white", relative_scaling=.5).generate(text)
        plt.figure(figsize=(20, 10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=1)
        # plt.show()
        plt.savefig("clustering/wordclouds/wc_preference_{}".format(i))
    print('=' * 80)
    print("Clasificación por preferencias (hashtags):")
    print("{:>18}   {:<22}".format('Preferencia', 'Número de Usuarios'))
    print("{:>18}   {:<22}".format('Macristas', count_m))
    print("{:>18}   {:<22}".format('Sciolistas', count_s))
    print("{:>18}   {:<22}".format('Macri y Scioli', count_o1))
    print("{:>18}   {:<22}".format('Otros', count_o2))


def sorted_users_by_cluster(model):
    """ Devuelve un defaultdict de listas donde los indices son los numeros de
        cluster, y el valor de cada uno es la lista de usuarios que están en ese
        cluster, ordenados por importancia (pipe.score)
    """
    pipe = model.pipeline
    kmeans = pipe.steps[1][1]
    scores_bycl = defaultdict(list)
    for i, u in enumerate(model.users_list):
        scores_bycl[kmeans.labels_[i]].append((pipe.score([u]), i))

    sorted_users = defaultdict(list)
    for cl_id in scores_bycl.keys():
        score_index_list = sorted(scores_bycl[cl_id], reverse=True)
        sorted_indexes_list = list(list(zip(*score_index_list))[1])
        sorted_users[cl_id] = [model.users_list[index] for index in sorted_indexes_list]

    # dict of cl_id:user_objects list
    return sorted_users


def print_relevant_users(sorted_users_bycl, print_n):
    print('=' * 80)
    print("Usuarios más relevantes de cada cluster:")
    for cl_id, users in sorted_users_bycl.items():
        print("Cluster {}:".format(cl_id))
        print("{:>18}   {:<18}   {:<18}   {:<18}".format('Username', 'Id', 'Rt por', 'Rt a'))
        for u in users[:print_n]:
            # if len(u.retweeted_to) == 1:
            #     continue
            # loc = " ".join(u.location)
            # tokens = " ".join(u.user_tokens())
            # des = " ".join(u.description)
            rt_by = len(u.retweeted_by)
            rt_by = rt_by if rt_by != 1 else u.retweeted_by[0]
            rt_to = len(u.retweeted_to)
            rt_to = rt_to if rt_to != 1 else u.retweeted_to[0]
            print("{:>18}   {:<18}   {:<18}   {:<18}".format(
                u.screen_name, u.id, rt_by, rt_to)
            )
        print('-' * 80)


def most_relevant_features_by_cluster(model, take_n):
    print('=' * 80)
    print("Features más relevantes de cada cluster:")
    vect = model.pipeline.steps[0][1]
    kmeans = model.pipeline.steps[1][1]

    best_features = dict()
    for i, coord in enumerate(kmeans.cluster_centers_):
        l = sorted(zip(coord, range(len(coord))), reverse=True)[:take_n]
        best_features[i] = list(list(zip(*l))[1])

    for cl_id, cols in best_features.items():
        print("Cluster {}:".format(cl_id))
        print("{:>18}   {:<22}".format('Feature', 'Tipo'))
        for col in cols:
            feat = vect.column_to_feature(col)
            print("{:>18}   {:<22}".format(str(feat[1]), feat[0].name))
        print('-' * 80)


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
    sorted_users_bycl = sorted_users_by_cluster(model)
    plot_wordclouds_by_cluster(sorted_users_bycl)
    plot_wordclouds_of_preferences(model.users_list)
    most_relevant_features_by_cluster(model, 20)
    print_relevant_users(sorted_users_bycl, 50)
