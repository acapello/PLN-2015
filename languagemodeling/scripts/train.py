"""Train an n-gram model.

Usage:
  train.py -n <n> [-m <model>] -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
import sys
sys.path.append("../../")

import pickle
from docopt import docopt
from nltk.corpus import PlaintextCorpusReader
# from nltk.corpus import gutenberg
from languagemodeling.ngram import NGram, AddOneNGram


if __name__ == '__main__':

    opts = docopt(__doc__)

    # load the data
    # sents = gutenberg.sents('austen-emma.txt')
    corpus = PlaintextCorpusReader('../corpora/', 'training_corpus.txt')
    sents = corpus.sents()

    # order of the model
    n = int(opts['-n'])
    # model type
    m = str(opts['-m'])

    # train the model
    if m == "ngram":
        print "NGram Model selected"
        model = NGram(n, sents)
    elif m == "addone":
        print "AddOne Model selected"
        model = AddOneNGram(n, sents)
    else:
        print "Bad Model Type"
        print help()
        exit()

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()