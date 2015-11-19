"""Train an n-gram model.

Usage:
  train.py -n <n> [-m <model>] -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
                  interpolated: Interpolated N-grams with add-one smoothing.
                  backoff: N-grams with Back-off smoothing with discounting.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
#  You must be in the virtualenv ($ workon pln-2015) to run this script
# Attention: you must run this (every) script from PLN-2015/ directory

# For running this script from any path
# import os, sys
# script_dir = os.path.realpath(os.path.split(sys.argv[0])[0])
# # put corpus_dir in PlaintextCorpusReader function
# corpus_dir = os.path.join(script_dir, '../../corpus/spanish/')
# # PLN-2015 directory (for importing packages)
# sys.path.append(os.path.join(script_dir, '../../'))

import pickle
from docopt import docopt
from nltk.corpus import PlaintextCorpusReader
# from nltk.corpus import gutenberg
from languagemodeling.ngram import \
    NGram, AddOneNGram, InterpolatedNGram, BackOffNGram


if __name__ == '__main__':

    opts = docopt(__doc__)

    # load the data
    # sents = gutenberg.sents('austen-emma.txt')
    corpus = PlaintextCorpusReader('corpus/spanish', 'training.txt')
    sents = corpus.sents()

    # order of the model
    n = int(opts['-n'])
    # model type
    m = str(opts['-m'])
    filename = opts['-o']

    # train the model
    if m == "ngram":
        print("NGram Model selected")
        model = NGram(n, sents)
    elif m == "addone":
        print("AddOne NGram Model selected")
        model = AddOneNGram(n, sents)
    elif m == "interpolated":
        print("Interpolated NGram Model selected")
        model = InterpolatedNGram(n, sents, addone=True)
    elif m == "backoff":
        print("BackOff NGram Model selected")
        model = BackOffNGram(n, sents, addone=True)
    else:
        print("Bad Model Type")
        print(help())
        exit()

    print("n: %d\nOutput file: %s\n" % (n, filename))
    # save it
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
