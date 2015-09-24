"""
Generate natural language sentences using a language model.

Usage:
  generate.py -i <file> -n <n>
  generate.py -h | --help

Options:
  -i <file>     Language model file.
  -n <n>        Number of sentences to generate.
  -h --help     Show this screen.
"""

import sys
sys.path.append("../../")

import pickle
from docopt import docopt
from languagemodeling.ngram import NGramGenerator


if __name__ == '__main__':

    opts = docopt(__doc__)

    n = int(opts['-n'])
    i = str(opts['-i'])
    f = open(i, 'rb')
    model = pickle.load(f)

    generator = NGramGenerator(model)

    for _ in range(n):
        sent = generator.generate_sent()
        for token in sent:
            print(token, end=" ")

        print("\n")
