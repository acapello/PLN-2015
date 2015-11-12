from nltk.tree import Tree
from nltk.grammar import Nonterminal as N, induce_pcfg
from parsing.util import unlexicalize, lexicalize
from parsing.cky_parser import CKYParser


class UPCFG:
    """Unlexicalized PCFG.
    """

    def __init__(self, parsed_sents, start='sentence', horzMarkov=None):
        """
        parsed_sents -- list of training trees.
        """
        # Non-Terminal start symbol of the pcfg.
        # Be aware that the start symbol now is specified by the init parameter
        # 'start', and not the start label of the trees in parsed_sents
        self.start = N(start)
        self.horzMarkov = horzMarkov
        # saving repeated productions (for induce probabilities)
        productions = []
        for t in parsed_sents:
            unlex_t = unlexicalize(t.copy(deep=True))
            # Set node label
            unlex_t.set_label(start)
            unlex_t.chomsky_normal_form(horzMarkov=horzMarkov)
            # Not collapsing the Root (collapseRoot=False)
            unlex_t.collapse_unary(collapsePOS=True)
            productions += unlex_t.productions()

        self.pcfg = induce_pcfg(self.start, productions)
        self._probabilistic_productions = self.pcfg.productions()
        self._parser = CKYParser(self.pcfg)


    def productions(self):
        """Returns the list of UPCFG probabilistic productions.
        """
        # type: list(nltk.grammar.ProbabilisticProduction)
        return self._probabilistic_productions

    def parse(self, tagged_sent):
        """Parse a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        words, tags = zip(*tagged_sent)
        # Unlexicalized tree in CNF
        _, unlex_parse_tree = self._parser.parse(tags)

        if unlex_parse_tree is None:
            # Flat tree
            parse_tree = Tree(self.start.symbol(),
                    [Tree(tag, [word]) for word, tag in tagged_sent])
        else:
            # Undo CNF
            unlex_parse_tree.un_chomsky_normal_form()
            # Add words
            parse_tree = lexicalize(unlex_parse_tree, words)

        return parse_tree
