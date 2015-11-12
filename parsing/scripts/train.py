"""Train a parser.

Usage:
  train.py [-m <model>] [-n <n>] -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: flat]:
                  flat: Flat trees
                  rbranch: Right branching trees
                  lbranch: Left branching trees
                  upcfg: Unlexicalized probabilistic context free grammars
  -n <n>        Order of horizontal markovization
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
import sys
sys.path.append('../')
sys.path.append('../../')

from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader

from parsing.baselines import Flat, RBranch, LBranch
from parsing.upcfg import UPCFG


models = {
    'flat': Flat,
    'rbranch': RBranch,
    'lbranch': LBranch,
    'upcfg': UPCFG
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    print('\nLoading corpus...')
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('../../corpus/ancora-2.0/', files)

    print('Training model...')
    om, on = opts['-m'], opts['-n']
    if om == 'upcfg':
        n = None if on is None else int(on)
        print('UPCFG model selected n={}.'.format(n))
        model = models[om](corpus.parsed_sents(), horzMarkov=n)
    elif om in ['flat', 'rbranch', 'lbranch']:
        print(om + ' model selected.')
        model = models[om](corpus.parsed_sents())
    else:
        print('Bad model type.')
        exit()

    print('Saving...\n')
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
