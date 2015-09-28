# coding: latin1
# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log
from random import random

# 'Start' and 'end' marks for the beginning and the end of a sentence.
START = '<s>'
END = '</s>'


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
            sent = [START for _ in range(n - 1)] + sent + [END]
            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1

    def count(self, tokens):
        """ Count for an n-gram or (n-1)-gram.

            tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self.counts[tuple(tokens)]

    def cond_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token.

            token -- the token.
            prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        if not prev_tokens:
            prev_tokens = []

        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        num = self.counts[tuple(tokens)]
        denom = float(self.counts[tuple(prev_tokens)])

        res = 0
        if denom != 0:
            res = num / denom

        return res

    def sent_prob(self, sent):
        """ Probability of a sentence. Warning: subject to underflow problems.

            sent -- the sentence as a list of tokens.
        """
        n = self.n
        prev_tokens = [START for _ in range(n - 1)]
        sent = prev_tokens + sent + [END]

        sent_prob = 1
        for i in range(n - 1, len(sent)):
            # select the token and the n - 1 prev tokens
            token = sent[i]
            prev_tokens = sent[i - n + 1:i]
            sent_prob *= self.cond_prob(token, prev_tokens)

        return sent_prob

    def sent_log_prob(self, sent):
        """ Log-probability of a sentence.

            sent -- the sentence as a list of tokens.
        """
        n = self.n
        sent = [START for _ in range(self.n - 1)] + sent + [END]

        log_prob = 0
        for i in range(n - 1, len(sent)):
            token = sent[i]
            prev_tokens = sent[i - n + 1:i]
            cond_prob = self.cond_prob(token, prev_tokens)

            if cond_prob == 0:
                log_prob = float('-inf')
                break
            else:
                log_prob += log(cond_prob, 2)

        return log_prob

    def perplexity(self, sents):
        """ Perplexity of a list of sentences.

            sents -- the sentences as a list of lists of tokens.
        """
        return Eval(self, sents).perplexity


class NGramGenerator:

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self.model = model
        self.n = n = model.n
        # dict of (n-1 gram tuple: dict of (next_possible_token: probability))
        self.probs = probs = dict()
        self.sorted_probs = sorted_probs = dict()

        for t in model.counts:
            if len(t) == n:
                ngram = t
                token = ngram[n - 1]
                prev_tokens_tuple = ngram[:n - 1]
                if prev_tokens_tuple not in probs:
                    probs.update({prev_tokens_tuple: dict()})
                probs[prev_tokens_tuple].update(
                    {token: model.cond_prob(token, list(prev_tokens_tuple))}
                )

        for prev_tokens_tuple, probs_dict in probs.items():
            # Sorting in decreasing order by probabilities and alphabetically
            # if they are equal
            sorted_list = sorted(probs_dict.items(),
                                 key=lambda x: (-x[1], x[0]))
            sorted_probs.update({prev_tokens_tuple: sorted_list})

    def generate_token(self, prev_tokens=None):
        """ Randomly generate a token, given prev_tokens.

            prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        if not prev_tokens:
            prev_tokens = []

        assert len(prev_tokens) == n - 1

        # random float from 0 to 1
        u = random()
        next_possible_tokens = self.sorted_probs[tuple(prev_tokens)]

        token = ''
        c = 0
        for tk, prob in next_possible_tokens:
            c += prob
            if u <= c:
                token = tk
                break

        assert token != ''

        return token

    def generate_sent(self):
        """Randomly generate a sentence."""
        prev_tokens = [START for _ in range(self.n - 1)]
        sent = []

        x = self.generate_token(prev_tokens)
        while x != END:
            sent.append(x)
            prev_tokens = (prev_tokens + [x])[1:]
            x = self.generate_token(prev_tokens)

        return sent


class AddOneNGram(NGram):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self.n = n
        self.counts = counts = defaultdict(int)

        vocabulary = set({END})
        for sent in sents:
            vocabulary.update(set(sent))
            sent = [START for _ in range(n - 1)] + sent + [END]

            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1

        self.v = len(vocabulary)

    def V(self):
        """ Size of the vocabulary.
        """
        return self.v

    def cond_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token.

            token -- the token.
            prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        if not prev_tokens:
            prev_tokens = []

        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        num = self.counts[tuple(tokens)]
        denom = float(self.counts[tuple(prev_tokens)])

        return (num + 1) / (denom + self.v)


class SmoothedModel(NGram):
    """ Shared Methods of InterpolatedNGram and BackOffNGram,
        both use addone smoothing.
    """
    def qML(self, token, prev_tokens):
        prob = 0
        tokens = prev_tokens + [token]
        num = self.counts[tuple(tokens)]
        denom = float(self.counts[tuple(prev_tokens)])

        if len(prev_tokens) == 0 and self.addone:
            prob = (num + 1) / (denom + self.v)
        elif denom != 0:
            prob = num / denom

        return prob


class InterpolatedNGram(SmoothedModel):

    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        self.n = n
        self.addone = addone
        self.gamma = gamma
        self.v = None

        if gamma is None:
            total_sents = len(sents)
            # We select 10 percent of the training data (q at least 1) as held
            # out sents, to select an approx. of the best gamma for the model,
            # the one who gives the best (lower) perplexity value of the held
            # out sents.
            q = int(total_sents / 10.0) + 1
            held_out_sents = sents[total_sents - q:total_sents]
            training_sents = sents[0:total_sents - q]
            possible_gammas = [5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 250.0,
                               500.0, 750.0, 1000.0]
            self.counts, vocabulary = self._get_counts_and_voc(training_sents)
            if addone:
                self.v = len(vocabulary)

            best_gamma = 1.0
            self.gamma = best_gamma
            min_p = self.perplexity(held_out_sents)

            for g in possible_gammas:
                self.gamma = g
                p = self.perplexity(held_out_sents)

                print("Gamma:", g, "Perplexity:", p)
                if p < min_p:
                    min_p = p
                    best_gamma = g

            self.gamma = best_gamma

        else:
            self.counts, vocabulary = self._get_counts_and_voc(sents)
            if addone:
                self.v = len(vocabulary)

        print("Gamma selected", self.gamma)

    def _get_counts_and_voc(self, sents):
        """ * Counts dict of 0-gram, 1-gram, ..., n-gram of sents
            * The vocabulary of the sents (if required)
        """
        n = self.n
        addone = self.addone
        counts = defaultdict(int)
        vocabulary = set({END})

        for sent in sents:
            if addone:
                vocabulary.update(set(sent))

            sent = [START for _ in range(n - 1)] + sent + [END]
            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i: i + n])
                for j in range(n + 1):
                    counts[ngram[:j]] += 1

            counts[(END,)] = len(sents)

        return counts, vocabulary

    def cond_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token.

            token -- the token.
            prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        gamma = self.gamma

        if not prev_tokens:
            prev_tokens = []
        assert len(prev_tokens) == n - 1

        op = 1
        res = 0
        for i in range(n - 1):
            prev_tokens = prev_tokens[i:]
            count = self.counts[tuple(prev_tokens)]
            l = op * (count / (count + gamma))
            op -= l
            cond_prob = self.qML(token, prev_tokens)
            res += l * cond_prob

        cond_prob = self.qML(token, [])
        res += op * cond_prob

        return res


class BackOffNGram(SmoothedModel):

    def __init__(self, n, sents, beta=None, addone=True):
        """
        Back-off NGram model with discounting as described by Michael Collins.

        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        beta -- discounting hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        self.n = n
        self.beta = beta
        self.addone = addone
        # The following attributes are calculated below
        self.v = None
        # Always type dict of float (dict()) during execution (alphas, denoms)
        self.alphas = None
        self.denoms = None
        # Always type defaultdict(set)
        self.Asets = None
        # Always type defaultdict(int)
        self.counts = None

        if beta is None:
            # When beta is not given, we calculate it similarly as the gamma
            # for the Interpolated model (here  0 < beta < 1).
            total_sents = len(sents)
            # 10 percent of the training data (at least one)
            q = int(total_sents / 10.0) + 1
            held_out_sents = sents[total_sents - q:total_sents]
            training_sents = sents[:total_sents - q]
            possible_betas = [0.1 * i for i in range(2, 10)]
            self.beta = best_beta = 0.1

            self.counts, self.Asets, vocabulary = \
                self._get_counts_Asets_and_voc(training_sents)
            if addone:
                self.v = len(vocabulary)

            self._calculate_alphas()
            self._calculate_denoms()

            min_p = self.perplexity(held_out_sents)
            for b in possible_betas:
                self.beta = b

                self._calculate_alphas()
                self._calculate_denoms()

                p = self.perplexity(held_out_sents)
                print("Beta:", b, "Perplexity:", p)
                if p < min_p:
                    min_p = p
                    best_beta = b

            self.beta = best_beta

        else:
            self.counts, self.Asets, vocabulary = \
                self._get_counts_Asets_and_voc(sents)
            if addone:
                self.v = len(vocabulary)

            self._calculate_alphas()
            self._calculate_denoms()

        print("Beta selected", self.beta)

    def _get_counts_Asets_and_voc(self, sents):
        """ * Counts dict of 0-gram, 1-gram, ..., n-gram of sents
            * Asets, the dict of (kgram: set(A(kgram)))
            * The vocabulary of the sents (if required, self.addone)
        """
        n = self.n
        addone = self.addone
        counts = defaultdict(int)
        Asets = defaultdict(set)
        vocabulary = set({END})

        for sent in sents:
            if addone:
                vocabulary.update(set(sent))

            sent = [START for _ in range(n - 1)] + sent + [END]
            sent_len = len(sent)
            counts[()] += sent_len - n + 1

            for k in range(1, n + 1):
                for i in range(sent_len - k):
                    kgram = tuple(sent[i:i + k])
                    counts[kgram] += 1
                    Asets[kgram].add(sent[i + k])

                kgram = tuple(sent[sent_len - k:sent_len])
                counts[kgram] += 1

        return counts, Asets, vocabulary

    def _calculate_alphas(self):
        """ Procedure for calculating the denoms used in cond_prob
            The result is saved in self.alphas as a dict of floats
            ONLY USE it after calculating the counts dict, and Asets
            Warning: This method changes the state of the object (self.alphas)
        """
        self.alphas = dict()
        for tokens in self.counts.keys():
            A = self.Asets[tokens]
            count = float(self.counts[tokens])
            A_len = len(A)
            if count != 0 and A_len != 0:
                self.alphas[tokens] = self.beta * A_len / count

    def _calculate_denoms(self):
        """ Procedure for calculating the alphas used in cond_prob
            The result is saved in self.alphas as a dict of floats
            ONLY USE it after calculating the counts dict, and Asets
            Warning: This method changes the state of the object (self.denoms),
            and use the logic of other funcions (self.cond_prob)
        """
        self.denoms = dict()
        for tokens in self.counts.keys():
            k = len(tokens)
            A = self.Asets[tokens]
            for i in range(1, k + 1):
                s = sum([self.cond_prob(t, tokens[k - i + 1:]) for t in A])
                self.denoms[tokens[k - i:]] = 1 - s

    def cond_prob(self, token, prev_tokens=None):
        """ Conditional probability of a token.

            token -- the token.
            prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if not prev_tokens:
            prev_tokens = []

        res = 0
        if len(prev_tokens) == 0:
            res = self.qML(token, prev_tokens)
        else:
            prev_tokens_tuple = tuple(prev_tokens)
            count = self.counts[prev_tokens_tuple + (token,)]

            if count > 0:
                res = (count - self.beta) / float(self.counts[prev_tokens_tuple])
            else:
                # get alpha, denom and return 1.0 as defect value
                alpha = self.alphas.get(prev_tokens_tuple, 1.0)
                denom = self.denoms.get(prev_tokens_tuple, 1.0)
                num = self.cond_prob(token, prev_tokens[1:])
                res = alpha * (num / denom)

        return res

    def A(self, tokens):
        """ Sets of words with counts > 0 and == 0 for a k-gram with 0 < k < n.

            tokens -- the k-gram tuple.
        """
        return self.Asets[tuple(tokens)]

    def alpha(self, tokens):
        """ Missing probability mass for a k-gram with 0 < k < n.

            tokens -- the k-gram tuple.
        """
        return self.alphas.get(tuple(tokens), 1.0)

    def denom(self, tokens):
        """ Normalization factor for a k-gram with 0 < k < n.

            tokens -- the k-gram tuple.
        """
        return self.denoms.get(tuple(tokens), 1.0)


class Eval(object):
    def __init__(self, model, test_sents):
        """ Class for evaluating a model.
            * log_probability, cross_entropy, perplexity
            model -- the model to be evaluated
            test_sents -- sents of the test corpus as a list of lists of tokens
        """
        M = 0
        log_probability = 0
        for sent in test_sents:
            M += len(sent)
            log_probability += model.sent_log_prob(sent)

        cross_entropy = log_probability / float(M)
        perplexity = pow(2, -cross_entropy)

        self.log_probability = log_probability
        self.cross_entropy = cross_entropy
        self.perplexity = perplexity
