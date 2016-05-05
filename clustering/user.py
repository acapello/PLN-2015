from clustering.tokenizer.happyfuntokenizing import word_re, Tokenizer
from unicodedata import normalize

function_words = {u'a', u'algo', u'alguien', u'alguna', u'algunas', u'algunos',
        u'ambos', u'aquel', u'aquella', u'aquellas', u'aquellos', u'aunque',
        u'cada', u'como', u'con', u'cosa', u'cual', u'cuales', u'cualquier',
        u'cualquiera', u'cuando', u'cuanta', u'cuantas', u'cuanto', u'cuantos',
        u'de', u'donde', u'dos', u'el', u'ella', u'ellas', u'ello', u'ellos',
        u'en', u'esa', u'esas', u'ese', u'esos', u'esta', u'estas', u'este',
        u'estos', u'hasta', u'la', u'las', u'le', u'les', u'lo', u'los', u'me',
        u'mi', u'mia', u'mias', u'mio', u'mios', u'mis', u'nadie', u'nos',
        u'nosotras', u'nosotros', u'o', u'para', u'pero', u'por', u'porque',
        u'pues', u'puesto', u'que', u'quien', u'quienes', u'se', u'si', u'sin',
        u'sobre', u'solamente', u'su', u'sus', u'suyo', u'tambien', u'te',
        u'ti', u'todas', u'todo', u'todos', u'tu', u'tus', u'tuyo', u'un',
        u'una', u'unas', u'uno', u'unos', u'usted', u'ustedes', u'y', u'yo',
        u'es', u'ya', u'al', u'del', u'hay', u'esto'}

def tokenize_text(text):
    if text is None:
        text = ''
    # TODO: quitar vocales repetidas de palabras
    t = Tokenizer()
    text = normalize('NFKD', text).encode('ASCII', 'ignore')
    tokenized = t.tokenize(text)
    # aca quitar letras repetidas
    tokens = []
    for t in tokenized:
        if t not in function_words and t[:4] != 'http':
            tokens.append(t)

    return tokens

def get_tweet_struct(tweet):
    tokens = tokenize_text(tweet['text'])
    favorite_count = int(tweet['favorite_count'])
    retweet_count = int(tweet['retweet_count'])
    d = {'tokens': tokens,
         'raw_tweet': tweet
        # much more
    }

    return d

class User:

    def __init__(self, tweet):

        self.id = tweet['user']['id']
        self.id_str = tweet['user']['id_str']
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
        self.update(tweet)

    def update(self, tweet):
        self.tweets.append(get_tweet_struct(tweet))
        for d in tweet['entities']['hashtags']:
            hashtag = normalize('NFKD', d['text']).encode('ASCII', 'ignore').lower()
            self.hashtags.add(hashtag)
