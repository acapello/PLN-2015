# coding: latin1
# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log


class NGram(object):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self.n = n
        self.counts = counts = defaultdict(int)

        for sent in sents:
            sent = ['<s>' for _ in xrange(n - 1)] + sent + ['</s>']

            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self.counts[tuple(tokens)]

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """

        n = self.n
        if not prev_tokens:
            prev_tokens = []

        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        num = float(self.counts[tuple(tokens)])
        denom = self.counts[tuple(prev_tokens)]

        res = 0
        if denom != 0:
            res = num / denom

        return res

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        n = self.n
        prev_tokens = ['<s>' for _ in xrange(self.n - 1)]
        sent = prev_tokens + sent + ['</s>']

        sent_prob = 1
        for i in xrange(n - 1, len(sent)):
            token = sent[i]
            prev_tokens = sent[i - n + 1:i]
            sent_prob *= self.cond_prob(token, prev_tokens)

        return sent_prob

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        n = self.n
        sent = ['<s>' for _ in xrange(self.n - 1)] + sent + ['</s>']

        log_prob = 0
        for i in xrange(n - 1, len(sent)):
            token = sent[i]
            prev_tokens = sent[i - n + 1:i]
            cond_prob = self.cond_prob(token, prev_tokens)
            if cond_prob == 0:
                log_prob = float('-inf')
                break
            else:
                log_prob += log(cond_prob, 2)

        return log_prob
