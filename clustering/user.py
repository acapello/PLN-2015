from clustering.tokenizer.happyfuntokenizing import word_re, Tokenizer
from unicodedata import normalize
import re
from clustering.data import function_words

def tokenize_text(text):
    if text is None:
        text = ''
    # TODO: quitar vocales repetidas de palabras
    t = Tokenizer()
    text = normalize('NFKD', text).encode('ASCII', 'ignore')

    tokenized = t.tokenize(text)
    # aca quitar letras repetidas
    tokens = []
    for token in tokenized:
        token = re.sub(r'[^\w]', '', token) #quita simbolos
        if token not in function_words and not token.isnumeric() and token[:4] != 'http':
            if token != '':
                tokens.append(token)

    return tokens

def get_tweet_struct(tweet):
    tokens = tokenize_text(tweet['text'])
    favorite_count = int(tweet['favorite_count'])
    retweet_count = int(tweet['retweet_count'])
    hashtag_list = tweet['entities']['hashtags']
    hashtags = [hashtag_list[i]['text'] for i in range(len(hashtag_list))]
    d = {'tokens': tokens, # token list for the tweet without function words
         'favorite_count': favorite_count,
         'retweet_count': retweet_count,
         'hashtags': hashtags,
         # 'raw_tweet': tweet
    }

    return d

class User:

    def __init__(self, tweet):

        self.id = tweet['user']['id']           #int
        self.id_str = tweet['user']['id_str']   #str
        self.description = tokenize_text(tweet['user']['description'])
        self.followers_count = int(tweet['user']['followers_count']) # (seguidores)
        self.friends_count = int(tweet['user']['friends_count']) # (seguidos)
        self.location = tokenize_text(tweet['user']['location'])
        self.name = tokenize_text(tweet['user']['name'])
        self.screen_name = tweet['user']['screen_name']
        self.verified = bool(tweet['user']['verified'])

        # tweet tokenizado y metadata interesante del tweet
        self.tweets = []
        self.hashtags = set()
        self.sum_favourites = 0
        self.sum_retweet_count = 0
        self.retweeted_by = []
        self.retweeted_to = []
        self.update(tweet)

    def update(self, tweet):
        tw = get_tweet_struct(tweet)
        self.tweets.append(tw)
        # update hashtags
        for h in tw['hashtags']:
            hashtag = normalize('NFKD', h).encode('ASCII', 'ignore').lower()
            self.hashtags.add(hashtag.decode('utf-8'))

        self.sum_favourites += tweet['favorite_count']
        self.sum_retweet_count += tweet['retweet_count']

    def user_tokens(self):
        tokens = []
        for tweet in self.tweets:
            tokens += tweet['tokens']

        return tokens