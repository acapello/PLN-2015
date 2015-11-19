"""
Evaulate a language model using the test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""
#  You must be in the virtualenv ($ workon pln-2015) to run this script
# Attention: you must run this (every) script from PLN-2015/ directory

import pickle
from docopt import docopt
from nltk.corpus import PlaintextCorpusReader
from languagemodeling.ngram import Eval


if __name__ == '__main__':

    opts = docopt(__doc__)

    i = str(opts['-i'])
    f = open(i, 'rb')
    model = pickle.load(f)

    test_corpus = PlaintextCorpusReader('corpus/spanish', 'test.txt')
    test_sents = test_corpus.sents()

    evaluator = Eval(model, test_sents)
    log_prob = evaluator.log_probability
    cross_ent = evaluator.cross_entropy
    perp = evaluator.perplexity

    print("Input filename: %s" % i)
    print(" Log-Probability: %f\n Cross-Entropy: %f\n Perplexity: %f\n"
          % (log_prob, cross_ent, perp))
