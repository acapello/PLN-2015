from collections import defaultdict, Counter


class BaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        self.voc = set()
        self.set_of_tags = set()
        self.tag_freq = Counter()
        self.most_freq_tag_by_word = defaultdict(str)
        tagsby_word = defaultdict(lambda: Counter())

        for sent in tagged_sents:
            for word, tag in sent:
                self.voc.add(word)
                self.set_of_tags.add(tag)
                self.tag_freq[tag] += 1
                tagsby_word[word][tag] += 1

        for w, tag_dict in tagsby_word.items():
            self.most_freq_tag_by_word[w] = tag_dict.most_common(1)[0][0]

        self.most_freq_tag = self.tag_freq.most_common(1)[0][0]

    def tagset(self):
        """Returns the set of tags.
        """
        return self.set_of_tags

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w not in self.voc

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        tag = None

        if self.unknown(w):
            tag = self.most_freq_tag
        else:
            tag = self.most_freq_tag_by_word[w]

        return tag

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        tagging = [self.tag_word(w) for w in sent]
        return tagging
