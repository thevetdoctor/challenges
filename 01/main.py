from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value

WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

print(max_word_value(WORDS))