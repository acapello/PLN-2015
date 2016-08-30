# encoding: utf-8

"""Evaulate a model.

Usage:
  print_relevant_users.py -i <file> -n <n_users> -c <cl_id>
  print_relevant_users.py -h | --help

Options:
  -i <file>     Model file.
  -n <n_users>  Number of users to show.
  -c <cl_id>    Cluster id to show.
  -h --help     Show this screen.
"""

from docopt import docopt
import pickle
from clustering.scripts.print_user_data import print_user_data
from clustering.scripts.eval import sorted_users_by_cluster


def print_relevant_users(model, n, cl_id):
    users = sorted_users_by_cluster(model)[cl_id]
    for u in users[:n]:
        print_user_data(u)
        print()

if __name__ == '__main__':
    opts = docopt(__doc__)

    filename = opts['-i']
    n = int(opts['-n'])
    cl_id = int(opts['-c'])

    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    print_relevant_users(model, n, cl_id)
