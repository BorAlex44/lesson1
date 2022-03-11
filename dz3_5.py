import random

def get_jokes(n, no_repeat=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    jokes = []
    """ Using the choice function, we select a random number from the lists """
    while i < n:
        rand_nous = random.choice(nouns)
        rand_adverbs = random.choice(adverbs)
        rand_adjectives = random.choice(adjectives)
        joke = f'{rand_nous} {rand_adverbs} {rand_adjectives}'
        jokes.append(joke)
        """ We remove the used words from the list """
        if no_repeat:
            nouns.remove(rand_nous)
            adverbs.remove(rand_adverbs)
            adjectives.remove(rand_adjectives)
            if not nouns or not adverbs or not adjectives:
                break
        i +=1
    print(jokes)

get_jokes(5, no_repeat=True)


