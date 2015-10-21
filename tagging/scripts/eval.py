"""Evaulate a tagger.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Tagging model file.
  -h --help     Show this screen.
"""
import sys
sys.path.append("../../")

# Warning: ignoring warnings
import warnings
warnings.filterwarnings('ignore')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    print("\nLoading the model...")
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()
    print("Model type: %s" % type(model))

    # load the data
    print("Loading corpus data...")
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('../../corpus/ancora-2.0/', files)
    sents = list(corpus.tagged_sents())

    # compute statistics
    print("Computing results...")
    # Compute Accuracy
    # Global accuracy of the model (percentage of right tagging)
    acc, hits, total = 0.0, 0, 0
    # Accuracy over known(k) and unknowns(u) words for the model
    hits_k, total_k, hits_u, total_u = 0, 0, 0, 0
    y_true, y_pred = [], []

    # Data for Confusion Matrix
    tagset = set()
    for t_sent in sents:
        for _, tag in t_sent:
            tagset.add(tag)
    tagset.update(model.tagset())

    # Count hits (model tagging vs original)
    n = len(sents)
    for i, sent in enumerate(sents):
        word_sent, gold_tag_sent = zip(*sent)

        model_tag_sent = list(model.tag(word_sent))
        assert len(model_tag_sent) == len(gold_tag_sent), i

        # Counting the hits (right tagging 1 and wrong tagging 0)
        model_vs_gold = enumerate(zip(model_tag_sent, gold_tag_sent))
        for j, (model_tag, gold_tag) in model_vs_gold:
            y_pred.append(model_tag)
            y_true.append(gold_tag)

            word = word_sent[j]
            is_hit = model_tag == gold_tag
            if model.unknown(word):
                hits_u += is_hit
                total_u += 1
            else:
                hits_k += is_hit
                total_k += 1
            hits += is_hit

        # Scores
        total += len(sent)
        acc = float(hits) / total

        # Comment this 2 lines if you are saving the results in a file
        # progress('Progress: {:3.1f}% (Accuracy: {:2.2f}%)'
        #          .format(float(i) * 100 / n, acc * 100))

    acc = float(hits) / total
    print("\nResults:")
    print('Global Accuracy: {:2.2f}%'.format(acc * 100))
    if total_k:
        acc_k = float(hits_k) / total_k
        print('Accuracy over known words: {:2.2f}%'.format(acc_k * 100))
    else:
        print('No known words for the model')

    if total_u:
        acc_u = float(hits_u) / total_u
        print('Accuracy over unknown words: {:2.2f}%'.format(acc_u * 100))
    else:
        print('No unknown words for the model')

    # print and plot the confusion matrix

    # adding labels for printing
    sorted_tags = sorted(list(tagset))
    cm = confusion_matrix(y_true=y_true, y_pred=y_pred, labels=sorted_tags)
    values_matrix = [list(arr) for arr in cm]
    matrix = [[''] + sorted_tags]
    for i, t in enumerate(sorted_tags):
        matrix.append([t] + values_matrix[i])

    # print the matrix
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    # add/rm a space in '' for more clarity (need more space)
    fmt = ' '.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    # print("Confusion Matrix:")
    # print('\n'.join(table))
    fl = '{}-confusion-matrix'.format(filename)
    # Save values in .txt
    g = open(fl + '.txt', 'w')
    g.write('\n'.join(table))
    g.close()

    # plot the matrix with labels (zoom in to see better)
    plt.matshow(cm)
    matplotlib.rcParams.update({'font.size': 4.5})
    plt.title('Confusion matrix', fontsize=12)
    plt.colorbar()
    plt.grid(linestyle=':', linewidth=0.2)
    plt.ylabel('True label', fontsize=12)
    plt.xlabel('Predicted label', fontsize=12)
    plt.xticks(np.arange(len(sorted_tags)), tuple(sorted_tags))
    plt.yticks(np.arange(len(sorted_tags)), tuple(sorted_tags))
    # save the plot
    plt.savefig(filename=fl + '.png', dpi=600)
    print('Confusion Matrix saved in ' + fl + '{.png, .txt}' + '\n')
