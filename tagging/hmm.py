# Use Python 3 interpreter and packages (math, functools)
from math import log2
from functools import reduce
from operator import mul
from collections import defaultdict

START = '<s>'
STOP = '</s>'
M_INF = float('-inf')


class HMM(object):

    def __init__(self, n, tagset, trans, out):
        """
        n -- n-gram size.
        tagset -- set of tags.
        trans -- transition probabilities dictionary.
        out -- output probabilities dictionary.
        """
        self.n = n
        self.set_of_tags = set(tagset)
        # q in Collins notes
        self.trans = dict(trans)
        # e in Collins notes
        self.out = dict(out)

    def tagset(self):
        """Returns the set of tags.
        """
        return self.set_of_tags

    def trans_prob(self, tag, prev_tags=None):
        """Probability of a tag.
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        if self.n == 1 and prev_tags is None:
            prev_tags = []
        assert len(prev_tags) == self.n - 1, (len(prev_tags), self.n - 1)
        # assert tag in self.tagset() | {STOP}
        # assert reduce(mul,
        #     [prev in self.tagset() | {START} for prev in prev_tags])
        possible_tags = self.trans.get(tuple(prev_tags), {})
        p = possible_tags.get(tag, 0.0)

        return p

    def out_prob(self, word, tag):
        """Probability of a word given a tag.
        word -- the word.
        tag -- the tag.
        """
        assert tag in self.tagset()
        possible_words = self.out.get(tag, {})
        p = possible_words.get(word, 0.0)

        return p

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.
        y -- tagging. (as a list of tags)
        """
        n = self.n
        y = [START] * (n - 1) + list(y) + [STOP]
        p = 1.0
        for i in range(n - 1, len(y)):
            tag = y[i]
            prev_tags = y[i - n + 1:i]
            trans_p = self.trans_prob(tag, prev_tags)
            p *= trans_p

        return p

    def _sent_tag_cond_prob(self, x, y):
        """ Productorial of out_prob, that is, the probability of
            a sentence given a tagging. e.g:
            e(the|D) × e(dog|N) × e(laughs|V) can be interpreted as the
            conditional probability p(the dog laughs|D N V STOP)
        """
        assert len(x) == len(y)
        return reduce(mul, [self.out_prob(w, t) for w, t in zip(x, y)])

    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.
        x -- sentence.
        y -- tagging.
        """
        assert len(x) == len(y)
        tag_p = self.tag_prob(y)
        cond_p = self._sent_tag_cond_prob(x, y)

        return tag_p * cond_p

    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.
        y -- tagging.
        """
        n = self.n
        y = [START] * (n - 1) + list(y) + [STOP]
        log_p = 0.0
        for i in range(n - 1, len(y)):
            trans_p = self.trans_prob(y[i], y[i - n + 1:i])
            if trans_p > 0.0:
                log_p += log2(trans_p)
            else:
                log_p = M_INF
                break

        return log_p

    def _sent_tag_log_prob(self, x, y):
        """
        Log-probability of a sent-tagging cond prob.
        y -- tagging.
        """
        log_p = 0.0
        for i in range(len(x)):
            out_p = self.out_prob(x[i], y[i])
            if out_p > 0.0:
                log_p += log2(out_p)
            else:
                log_p = M_INF
                break

        return log_p

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
        x -- sentence.
        y -- tagging.
        """
        assert len(x) == len(y)
        log_tagging = self.tag_log_prob(y)
        log_sent_tagg = self._sent_tag_log_prob(x, y)

        return log_tagging + log_sent_tagg

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
        sent -- the sentence.
        """
        tagger = ViterbiTagger(self)
        return tagger.tag(sent)


class MLHMM(HMM):

    def __init__(self, n, tagged_sents, addone=True):
        """
        n -- order of the model.
        tagged_sents -- training sentences, each one being a list of pairs.
        addone -- whether to use addone smoothing (default: True).
        """

        self.n = n
        self.addone = addone
        # vocabulary. set(strings)
        self.voc = voc = set()
        # tagset. set(strings)
        # dict of tuples (of tags) of len n-1 and n and its counts in corpus
        self.tags_counts = tags_counts = defaultdict(int)
        # len of each tag (len 1)
        self.one_tag_count = one_tag_count = defaultdict(int)
        # count of paired(word, tag) in the corpus. dict{2_uple: count}
        self.w_t_counts = w_t_counts = defaultdict(int)

        for t_sent in tagged_sents:
            # for the ML estimate for self.out and self.trans
            for word, tag in t_sent:
                w_t_counts[(word, tag)] += 1
                one_tag_count[tag] += 1
                voc.add(word)

            tags = [START] * (n - 1) + [tag for _, tag in t_sent] + [STOP]
            for i in range(len(tags) - n + 1):
                ntags = tuple(tags[i:i + n])
                tags_counts[ntags] += 1
                tags_counts[ntags[:-1]] += 1

        self.set_of_tags = set(self.one_tag_count.keys())

    def tagset(self):
        """Returns the set of tags.
        """
        return self.set_of_tags

    def tcount(self, tokens):
        """Count for a k-gram for k <= n.

        tokens -- the k-gram tuple.
        """
        return self.tags_counts[tuple(tokens)]

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w not in self.voc

    def trans_prob(self, tag, prev_tags=None):
        """Probability of a tag.
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        if self.n == 1 and prev_tags is None:
            prev_tags = []
        # assert len(prev_tags) == self.n - 1, (len(prev_tags), self.n - 1)
        assert tag in self.tagset() | {STOP}
        # assert reduce(mul,
        #     [prev in self.tagset() | {START} for prev in prev_tags])
        prev_tags = tuple(prev_tags)
        num = self.tags_counts[prev_tags + (tag, )]
        denom = float(self.tags_counts[prev_tags])

        res = 0.0
        if self.addone:
            # should be len(self.voc) but changed for better performance
            res = (num + 1) / (denom + len(self.tagset()))
        elif denom != 0:
            res = num / denom

        return res

    def out_prob(self, word, tag):
        """Probability of a word given a tag.
        word -- the word.
        tag -- the tag.
        """
        assert tag in self.tagset()
        res = 0.0
        if word in self.voc:
            num = self.w_t_counts[(word, tag)]
            denom = float(self.one_tag_count[tag])
            if denom != 0:
                res = num / denom
        else:
            res = 1.0 / len(self.voc)

        return res


class ViterbiTagger(object):

    def __init__(self, hmm):
        """
        hmm -- the HMM.
        """
        self.hmm = hmm
        self._pi = {}

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.

        sent -- the sentence.
        """
        sent = list(sent)
        hmm = self.hmm
        tagset = hmm.tagset()
        self._pi = pi = {0: {(START,) * (hmm.n - 1): (log2(1.0), [])}}

        for k, w in enumerate(sent):
            pi[k + 1] = {}
            tag_out_probs = [(t, hmm.out_prob(w, t)) for t in tagset]
            for t, out_p in [(t, p) for t, p in tag_out_probs if p > 0.0]:
                for prev_tags, (log_p, tag_sent) in pi[k].items():
                    trans_p = hmm.trans_prob(t, prev_tags)
                    if trans_p > 0.0:
                        ts = (prev_tags + (t,))[1:]
                        new_lp = log_p + log2(trans_p) + log2(out_p)
                        if ts not in pi[k + 1] or new_lp > pi[k + 1][ts][0]:
                            pi[k + 1][ts] = (new_lp, tag_sent + [t])

        max_lp = M_INF
        res = None
        for prev_tags, (log_p, tagging) in pi[len(sent)].items():
            trans_p = hmm.trans_prob(STOP, prev_tags)
            if trans_p > 0:
                new_lp = log_p + log2(trans_p)
                if new_lp > max_lp:
                    max_lp = new_lp
                    res = tagging

        return res
