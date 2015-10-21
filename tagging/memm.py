# Scikit Learn Pupeline
from sklearn.pipeline import Pipeline
# Feature Vectorizer
from featureforge.vectorizer import Vectorizer
# Classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
# History
from tagging.features import (History, word_lower, word_istitle, word_isupper,
                              word_isdigit, NPrevTags, PrevWord)


START = '<s>'
STOP = '</s>'
# must change train.py in case of modifying this
classifiers = {'logreg': LogisticRegression,
               'nb': MultinomialNB,
               'svc': LinearSVC}


class MEMM:

    def __init__(self, n, tagged_sents, classifier='logreg'):
        """
        n -- order of the model.
        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        self.n = n
        self.set_of_tags = set()
        self.voc = set()
        for t_sent in tagged_sents:
            for word, tag in t_sent:
                self.set_of_tags.add(tag)
                self.voc.add(word)

        features = [word_lower, word_istitle, word_isupper, word_isdigit]
        features += [PrevWord(f) for f in features]
        features += [NPrevTags(i) for i in range(1, n - 1)]

        vect = Vectorizer(features)
        clf = classifiers[classifier]()
        self.pipeline = Pipeline(steps=[('vect', vect), ('clf', clf)])

        histories = self.sents_histories(tagged_sents)
        tags = self.sents_tags(tagged_sents)
        self.pipeline.fit(histories, tags)

    def tagset(self):
        """Returns the set of tags.
        """
        return self.set_of_tags

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w in self.voc

    def sents_histories(self, tagged_sents):
        """
        Iterator over the histories of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        hs = list()
        for t_sent in tagged_sents:
            hs += [h for h in self.sent_histories(t_sent)]

        return hs

    def sent_histories(self, tagged_sent):
        """
        Iterator over the histories of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """

        n = self.n
        sent, tags = zip(*tagged_sent) if len(tagged_sent) != 0 else ((), ())
        sent = list(sent)
        tags = (START, ) * (n - 1) + tags
        return [History(sent, tags[i:i + n - 1], i) for i in range(len(sent))]

    def sents_tags(self, tagged_sents):
        """
        Iterator over the tags of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        tags = list()
        for t_sent in tagged_sents:
            tags += [tag for _, tag in t_sent]

        return tags

    def sent_tags(self, tagged_sent):
        """
        Iterator over the tags of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        return [tag for _, tag in tagged_sent]

    def tag_history(self, h):
        """Tag a history.

        h -- the history.
        """
        return self.pipeline.predict([h])[0]

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        n = self.n
        prev_tags = (START, ) * (n - 1)
        tagging = []
        for i in range(len(sent)):
            h = History(sent=sent, prev_tags=prev_tags, i=i)
            tag = self.tag_history(h)
            prev_tags = (prev_tags + (tag, ))[1:]
            tagging.append(tag)

        return tagging
