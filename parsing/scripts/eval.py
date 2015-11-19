"""Evaulate a parser.

Usage:
  eval.py [-m <m>] [-n <n>] -i <file>
  eval.py -h | --help

Options:
  -m <m>        Evaluate only sentences of length less than or equal m.
  -n <n>        Evaluate only the first n sentences.
  -i <file>     Parsing model file.
  -h --help     Show this screen.
  Note: m and n can be used together to satisfy both conditions at the same\
 time
"""
# import sys
# sys.path.append('../../')
from docopt import docopt
import pickle
import sys
from corpus.ancora import SimpleAncoraCorpusReader
from parsing.util import spans


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg) + 1
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    print('\nLoading model...')

    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()
    print("Model type: %s" % type(model))

    print('Loading corpus...')

    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('corpus/ancora-2.0/', files)
    parsed_sents = list(corpus.parsed_sents())

    om, on = opts['-m'], opts['-n']
    m = int(om) if om else float('+inf')
    n = int(on) if on else len(parsed_sents)
    parsed_sents = [t for t in parsed_sents[:n] if len(t.leaves()) <= m]
    n = len(parsed_sents)

    print('Parsing...')

    hits_l, total_gold_l, total_model_l = 0, 0, 0
    prec_l, rec_l, f1_l = 0, 0, 0
    prec_u, rec_u, f1_u = 0, 0, 0
    hits_u, total_gold_u, total_model_u = 0, 0, 0

    format_str = '{:3.1f}% ({}/{}) | Labeled: (P={:2.2f}%, R={:2.2f}%, \
F1={:2.2f}%) | Unlabeled: (P={:2.2f}%, R={:2.2f}%, F1={:2.2f}%)'
    # Uncomment next line if you want to see the progress
    # progress(format_str.format(0.0, 0, n, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

    for i, gold_parsed_sent in enumerate(parsed_sents):
        tagged_sent = gold_parsed_sent.pos()

        # parse
        model_parsed_sent = model.parse(tagged_sent)

        # compute labeled scores
        gold_spans_l = spans(gold_parsed_sent, unary=False)
        model_spans_l = spans(model_parsed_sent, unary=False)
        hits_l += len(gold_spans_l & model_spans_l)
        total_gold_l += len(gold_spans_l)
        total_model_l += len(model_spans_l)

        # compute labeled partial results
        prec_l = float(hits_l) / total_model_l * 100
        rec_l = float(hits_l) / total_gold_l * 100
        if (prec_l + rec_l) > 0:
            f1_l = 2 * prec_l * rec_l / (prec_l + rec_l)

        # compute labeled scores
        gold_spans_u = {(j, k) for (n, j, k) in gold_spans_l}
        model_spans_u = {(j, k) for (n, j, k) in model_spans_l}
        hits_u += len(gold_spans_u & model_spans_u)
        total_gold_u += len(gold_spans_u)
        total_model_u += len(model_spans_u)

        # compute labeled partial results
        prec_u = float(hits_u) / total_model_u * 100
        rec_u = float(hits_u) / total_gold_u * 100
        if (prec_l + rec_l) > 0:
            f1_u = 2 * prec_u * rec_u / (prec_u + rec_u)

        # Uncomment next lines if you want to see the progress
        # progress(format_str.format(float(i+1) * 100 / n, i+1, n,
        #          prec_l, rec_l, f1_l,  prec_u, rec_u, f1_u))

    print('')
    print('Parsed {} sentences'.format(n))
    print('Labeled')
    print('  Precision: {:2.2f}% '.format(prec_l))
    print('  Recall: {:2.2f}% '.format(rec_l))
    print('  F1: {:2.2f}% '.format(f1_l))
    print('Unlabeled')
    print('  Precision: {:2.2f}% '.format(prec_u))
    print('  Recall: {:2.2f}% '.format(rec_u))
    print('  F1: {:2.2f}% '.format(f1_u))
    print('')
