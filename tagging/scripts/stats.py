"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
import sys
sys.path.append("../../")

from docopt import docopt
from collections import defaultdict, Counter

from corpus.ancora import SimpleAncoraCorpusReader


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    corpus = SimpleAncoraCorpusReader('../../corpus/ancora-2.0/')
    sents = list(corpus.tagged_sents())

    # compute the statistics
    words_len = 0
    word_freq = Counter()
    tag_freq = Counter()
    wordsby_tag = defaultdict(lambda: Counter())
    tagsby_word = defaultdict(lambda: defaultdict(int))

    for sent in sents:
        words_len += len(sent)
        for word, tag in sent:
            word_freq[word] += 1
            tag_freq[tag] += 1
            wordsby_tag[tag][word] += 1
            tagsby_word[word][tag] += 1

    print('-----Estadísticas básicas:------------------------------------------\
-------')
    print('\tCantidad de oraciones: {}'.format(len(sents)))
    print('\tCantidad de ocurrencias de palabras: {}'.format(words_len))
    print('\tCantidad de palabras (vocabulario): {}'.format(len(tagsby_word)))
    print('\tCantidad de etiquetas (vocabulario de tags): {}\n'
          .format(len(wordsby_tag)))

    print('-----Etiquetas más frecuentes:--------------------------------------\
-------')
    for tag, freq in tag_freq.most_common(10):
        # Frequency of the tag in the corpus and percentage of the total
        print('\tEtiqueta: \'{0}\'  Frecuencia: {1}  \
Porcentaje del total: {2:.2f}'
              .format(tag, freq, 100 * freq / float(words_len)))
        print('\tPalabras más frecuentes con la etiqueta \'%s\':' % tag)
        five_largest = wordsby_tag[tag].most_common(5)
        for word, freq in five_largest:
            print('\t\t' + word + ' : ' + str(freq))
        print()

    print('\n-----Niveles de ambigüedad de las palabras:-----------------------\
-------')

    # Saving ambiguity levels (words seen with one or more tags in the corpus)
    c = defaultdict(lambda: Counter())
    for word, tag_dict in tagsby_word.items():
        c[len(tag_dict)][word] = word_freq[word]

    for ambiguity in range(1, 10):
        # Ambiguity level,frequency and percentage of the total
        freq = len(c[ambiguity])
        print('\tAmbigüedad: {0}  Cantidad de palabras: {1}  \
Porcentaje del total: {2:.2f}'
              .format(ambiguity, freq, 100 * freq / float(len(tagsby_word))))

        five_largest = c[ambiguity].most_common(5)
        if freq > 0:
            print('\tPalabras más frecuentes con ambigüedad %d:' % ambiguity)
            for word, freq in five_largest:
                print('\t\t' + word + ' : ' + str(freq))
        print()
