import json # 'loads' used

def get_tweets():
    """ Obtener tweets (puros por el momento (sin RT))
        Devuelve una lista de diccionarios, donde cada diccionario es un tweet
        con toda su info. (entre ella el texto y el usuario)
    """
    f = open('clustering/corpus/tweets-balotaje1.txt', 'r')
    g = open('clustering/corpus/tweets-balotaje2.txt', 'r')
    h = open('clustering/corpus/tweets-balotaje3.txt', 'r')
    s = f.read() + g.read() + h.read()
    sp = s.split('\n')
    ts = [sp[i] for i in range(len(sp)) if i % 2 == 0 and sp[i] != '']
    tweets = []
    for t in ts:
        d = json.loads(t)
        a = d.get('text', '')
        if len(a) > 2 and a[:2] != 'RT':
            tweets.append(d)

    return tweets