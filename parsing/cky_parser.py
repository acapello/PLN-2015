from nltk.tree import Tree
from nltk.grammar import Nonterminal as N
from collections import defaultdict


class CKYParser:

    def __init__(self, grammar):
        """
        grammar -- a binarised NLTK PCFG.
        """
        assert grammar.is_binarised()

        self.grammar = grammar
        self.start_sym = grammar.start().symbol()
        self._pi = defaultdict(dict)
        self._bp = defaultdict(dict)

        # Dicts with logprobs of lexical and unlexical productions
        self.prods_lps_lex = ps_lex = defaultdict(dict)
        self.prods_lps_unlex = ps_unlex = defaultdict(dict)
        for p in grammar.productions():
            # a str
            lhs = N.symbol(p.lhs())
            # a tuple of str
            rhs = p.rhs()
            if p.is_lexical():
                ps_lex[rhs][lhs] = p.logprob()
            else:
                rhs = tuple(map(N.symbol, p.rhs()))
                ps_unlex[rhs][lhs] = p.logprob()

    def parse(self, sent):
        """Parse a sequence of terminals.

        sent -- the sequence of terminals.
        """
        # CKY parsing algorithm
        prods_lps_lex = self.prods_lps_lex
        prods_lps_unlex = self.prods_lps_unlex
        self._pi = pi = defaultdict(dict)
        self._bp = bp = defaultdict(dict)

        # Initialization
        for i, w in enumerate(sent, start=1):
            for X, lp in prods_lps_lex[(w, )].items():
                pi[(i, i)][X] = lp
                bp[(i, i)][X] = Tree(X, [w])

        # Algorithm
        n = len(sent)
        for l in range(1, n):
            for i in range(1, n - l + 1):
                j = i + l
                pi[(i, j)] = {}
                bp[(i, j)] = {}
                for s in range(i, j):
                    # both lists of strings (symbols)
                    possibleYs = pi[(i, s)].keys()
                    possibleZs = pi[(s + 1, j)].keys()
                    for Y in possibleYs:
                        for Z in possibleZs:
                            # finding X such that exist a rule X -> Y Z
                            # list of pairs (str, logprob)
                            possible_Xs_lp = prods_lps_unlex[(Y, Z)].items()
                            for X, lp in possible_Xs_lp:
                                pi_Y = pi[(i, s)][Y]
                                pi_Z = pi[(s + 1, j)][Z]
                                new_lp = (lp + pi_Y + pi_Z)

                                # add new_lp and add tree from rule X -> Y Z
                                if new_lp > pi[(i, j)].get(X, float('-inf')):
                                    pi[(i, j)][X] = new_lp
                                    st_l = bp[(i, s)][Y]
                                    st_r = bp[(s + 1, j)][Z]
                                    subtree = [st_l, st_r]
                                    bp[(i, j)][X] = Tree(X, subtree)

        best_lp = pi[(1, n)].get(self.start_sym, float('-inf'))
        best_parse_tree = bp[1, n].get(self.start_sym, None)

        return (best_lp, best_parse_tree)
