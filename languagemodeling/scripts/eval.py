"""
Evaulate a language model using the test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""

import sys
sys.path.append("/home/agustin/pln/PLN-2015")

import pickle
from docopt import docopt
from nltk.corpus import PlaintextCorpusReader


if __name__ == '__main__':

    opts = docopt(__doc__)

    i = str(opts['-i'])
    f = open(i, 'rb')
    model = pickle.load(f)

    test_corpus = PlaintextCorpusReader('../corpora/', 'test_corpus.txt')
    sents = test_corpus.sents()

    M = 0
    log_probability = 0
    for sent in sents:
        M += len(sent)
        log_probability += model.sent_log_prob(sent)

    cross_entropy = log_probability / float(M)
    perplexity = pow(2, -cross_entropy)

    print "\n Log-Probability: %f\n Cross-Entropy: %f\n Perplexity: %f\n" \
        % (log_probability, cross_entropy, perplexity)
