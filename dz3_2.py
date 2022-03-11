word_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}


def num_translate_adv(num_word):
    word = word_dict.get(num_word.lower())
    if word:
        return word.capitalize() if num_word[0].istitle() else word


print(num_translate_adv('Seven'))
