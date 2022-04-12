'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
№>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''
from random import choice

def get_jokes(count, repeat = True):
    """Return the selected number of jokes."""

    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(count):
        if not repeat:
            nouns_string, adverbs_string, adjectives_string = (choice(nouns)), (choice(adverbs)), (choice(adjectives))
            jokes.append(f'{nouns_string} {adverbs_string} {adjectives_string}')
            nouns.remove(nouns_string)
            adverbs.remove(adverbs_string)
            adjectives.remove(adjectives_string)
        else:
            nouns_string, adverbs_string, adjectives_string = (choice(nouns)), (choice(adverbs)), (choice(adjectives))
            jokes.append(f'{nouns_string} {adverbs_string} {adjectives_string}')
    return jokes


if __name__ == "__main__":
    print(get_jokes(5, False))
