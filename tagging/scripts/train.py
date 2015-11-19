"""Train a sequence tagger.

Usage:
  train.py [-n <n>] [-m <model>] [-c <classifier>] -o <file>
  train.py -h | --help

Options:
  -n <n>           Order of the model [default: 1]
                    (models mlhmm and memm need it, base do not)
  -m <model>       Model to use [default: base]:
                    base: Baseline
                    mlhmm: Maximum Likelihood Hidden Markov Model
                    memm: Maximum Entropy Markov Model
  -c <classifier>  Classifier used in MEMM [default: logreg]
                    logreg: LogisticRegression
                    nb: MultinomialNB
                    svc: LinearSVC
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
# import sys
# sys.path.append("../../")

# Warning: ignoring warnings
import warnings
warnings.filterwarnings('ignore')

from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger
from tagging.hmm import MLHMM
from tagging.memm import MEMM

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    print("Loading corpus data...")
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('corpus/ancora-2.0/', files)
    sents = list(corpus.tagged_sents())

    # order of the model
    m = str(opts['-m'])
    # train the model
    filename = opts['-o']

    if m == "base":
        print("Baseline Model selected")
        model = BaselineTagger(tagged_sents=sents)
    elif m == "mlhmm":
        n = int(opts['-n'])
        print("Maximum Likelihood Hidden Markov Model selected, n=%d" % n)
        model = MLHMM(n=n, tagged_sents=sents, addone=True)
    elif m == 'memm':
        n = int(opts['-n'])
        c = str(opts['-c'])
        if c not in ['logreg', 'nb', 'svc']:
            print("Bad classifier type, use --help option for help")
            exit()
        print("Maximum Entropy Markov Model selected, n=%d, c=%s" % (n, c))
        model = MEMM(n=n, tagged_sents=sents, classifier=c)
    else:
        print("Bad model type, use --help option for help")
        exit()

    # save it
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
