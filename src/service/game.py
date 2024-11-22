import src.data.game as data
from collections import Counter, defaultdict


def get_word() -> str:
    return data.get_word()


def get_score(word: str, guess: str) -> str:
    word = word.lower()
    guess = guess.lower()
    HIT = 'H'
    MISS = 'M'
    CLOSE = 'C'
    length: int =len(word)
    if len(guess) != length:
        return 'ERROR'

    word_counter = Counter(word)
    guess_counter = defaultdict(int)
    result = [MISS] * length

    for pos, letter in enumerate(guess):
        if letter == word[pos]:
            result[pos] = HIT
            guess_counter[letter] += 1

    for pos, letter in enumerate(guess):
        if result[pos] == HIT:
            continue
        guess_counter[letter] += 1

        if (letter in word
                and guess_counter[letter] <= word_counter[letter]):
            result[pos] = CLOSE

    result = ''.join(result)
    return result
