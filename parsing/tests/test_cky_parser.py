# https://docs.python.org/3/library/unittest.html
import sys
sys.path.append('../../')

from unittest import TestCase
from math import log2

from nltk.tree import Tree
from nltk.grammar import PCFG

from parsing.cky_parser import CKYParser


class TestCKYParser(TestCase):

    def test_parse(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]
                NP -> Det Noun          [0.6]
                NP -> Noun Adj          [0.4]
                VP -> Verb NP           [1.0]
                Det -> 'el'             [1.0]
                Noun -> 'gato'          [0.9]
                Noun -> 'pescado'       [0.1]
                Verb -> 'come'          [1.0]
                Adj -> 'crudo'          [1.0]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('el gato come pescado crudo'.split())

        # check chart
        pi = {
            (1, 1): {'Det': log2(1.0)},
            (2, 2): {'Noun': log2(0.9)},
            (3, 3): {'Verb': log2(1.0)},
            (4, 4): {'Noun': log2(0.1)},
            (5, 5): {'Adj': log2(1.0)},

            (1, 2): {'NP': log2(0.6 * 1.0 * 0.9)},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': log2(0.4 * 0.1 * 1.0)},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S':
                     log2(1.0) +  # rule S -> NP VP
                     log2(0.6 * 1.0 * 0.9) +  # left part
                     log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},  # right part
        }
        self.assertEqualPi(parser._pi, pi)

        # check partial results
        bp = {
            (1, 1): {'Det': Tree.fromstring("(Det el)")},
            (2, 2): {'Noun': Tree.fromstring("(Noun gato)")},
            (3, 3): {'Verb': Tree.fromstring("(Verb come)")},
            (4, 4): {'Noun': Tree.fromstring("(Noun pescado)")},
            (5, 5): {'Adj': Tree.fromstring("(Adj crudo)")},

            (1, 2): {'NP': Tree.fromstring("(NP (Det el) (Noun gato))")},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': Tree.fromstring("(NP (Noun pescado) (Adj crudo))")},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': Tree.fromstring(
                "(VP (Verb come) (NP (Noun pescado) (Adj crudo)))")},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S': Tree.fromstring(
                """(S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                   )
                """)},
        }
        self.assertEqual(parser._bp, bp)

        # check tree
        t2 = Tree.fromstring(
            """
                (S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                )
            """)
        self.assertEqual(t, t2)

        # check log probability
        lp2 = log2(1.0 * 0.6 * 1.0 * 0.9 * 1.0 * 1.0 * 0.4 * 0.1 * 1.0)
        self.assertAlmostEqual(lp, lp2)

    def test_parse_2(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]
                NP -> NP PP             [0.5]
                NP -> Det Noun          [0.5]
                VP -> VP PP             [0.9]
                VP -> Verb NP           [0.1]
                PP -> Prep NP           [1.0]
                Noun -> 'dog'           [0.2]
                Noun -> 'man'           [0.2]
                Noun -> 'town'          [0.6]
                Verb -> 'saw'           [1.0]
                Prep -> 'in'            [1.0]
                Det -> 'the'            [1.0]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('the man saw the dog in the town'.split())

        # check chart
        pi = {
                 (1, 1): {'Det': log2(1.0)},
                 (2, 2): {'Noun': log2(0.2)},
                 (3, 3): {'Verb': log2(1.0)},
                 (4, 4): {'Det': log2(1.0)},
                 (5, 5): {'Noun': log2(0.2)},
                 (6, 6): {'Prep': log2(1.0)},
                 (7, 7): {'Det': log2(1.0)},
                 (8, 8): {'Noun': log2(0.6)},

                 (1, 2): {'NP': -3.321928094887362},
                 (2, 3): {},
                 (3, 4): {},
                 (4, 5): {'NP': -3.321928094887362},
                 (5, 6): {},
                 (6, 7): {},
                 (7, 8): {'NP': -1.736965594166206},

                 (1, 3): {},
                 (2, 4): {},
                 (3, 5): {'VP': -6.643856189774724},
                 (4, 6): {},
                 (5, 7): {},
                 (6, 8): {'PP': -1.736965594166206},

                 (1, 4): {},
                 (2, 5): {},
                 (3, 6): {},
                 (4, 7): {},
                 (5, 8): {},

                 (1, 5): {'S': -9.965784284662087},
                 (2, 6): {},
                 (3, 7): {},
                 (4, 8): {'NP': -6.058893689053567},

                 (1, 6): {},
                 (2, 7): {},
                 (3, 8): {'VP': -8.53282487738598},

                 (1, 7): {},
                 (2, 8): {},

                 (1, 8): {'S': -11.854752972273342},

                 }
        self.assertEqualPi(parser._pi, pi)

        bp = {
            (1, 1): {'Det': Tree.fromstring('(Det the)')},
            (2, 2): {'Noun': Tree.fromstring('(Noun man)')},
            (3, 3): {'Verb': Tree.fromstring('(Verb saw)')},
            (4, 4): {'Det': Tree.fromstring('(Det the)')},
            (5, 5): {'Noun': Tree.fromstring('(Noun dog)')},
            (6, 6): {'Prep': Tree.fromstring('(Prep in)')},
            (7, 7): {'Det': Tree.fromstring('(Det the)')},
            (8, 8): {'Noun': Tree.fromstring('(Noun town)')},
            (1, 2): {'NP': Tree.fromstring('(NP (Det the) (Noun man))')},

            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': Tree.fromstring('(NP (Det the) (Noun dog))')},
            (5, 6): {},
            (6, 7): {},
            (7, 8): {'NP': Tree.fromstring('(NP (Det the) (Noun town))')},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': Tree.fromstring(
                '(VP (Verb saw) (NP (Det the) (Noun dog)))')},
            (4, 6): {},
            (5, 7): {},
            (6, 8): {'PP': Tree.fromstring(
                '(PP (Prep in) (NP (Det the) (Noun town)))')},

            (1, 4): {},
            (2, 5): {},
            (3, 6): {},
            (4, 7): {},
            (5, 8): {},

            (1, 5): {'S': Tree.fromstring(
                """(S
                      (NP (Det the) (Noun man))
                      (VP (Verb saw) (NP (Det the) (Noun dog))))""")},
            (2, 6): {},
            (3, 7): {},
            (4, 8): {'NP': Tree.fromstring(
                """(NP
                      (NP (Det the) (Noun dog))
                      (PP (Prep in) (NP (Det the) (Noun town))))""")},
            (1, 6): {},
            (2, 7): {},
            (3, 8): {'VP': Tree.fromstring(
                """(VP
                      (VP (Verb saw) (NP (Det the) (Noun dog)))
                      (PP (Prep in) (NP (Det the) (Noun town))))""")},
            (1, 7): {},
            (2, 8): {},

            (1, 8): {'S': Tree.fromstring(
                """(S
                      (NP (Det the) (Noun man))
                      (VP
                        (VP (Verb saw) (NP (Det the) (Noun dog)))
                        (PP (Prep in) (NP (Det the) (Noun town)))))""")},
            }

        self.assertEqual(parser._bp, bp)

    def assertEqualPi(self, pi1, pi2):
        self.assertEqual(set(pi1.keys()), set(pi2.keys()))

        for k in pi1.keys():
            d1, d2 = pi1[k], pi2[k]
            self.assertEqual(d1.keys(), d2.keys(), k)
            for k2 in d1.keys():
                prob1 = d1[k2]
                prob2 = d2[k2]
                self.assertAlmostEqual(prob1, prob2)
