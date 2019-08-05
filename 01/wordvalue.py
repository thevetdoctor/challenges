from data import DICTIONARY, LETTER_SCORES

def load_words(DICTIONARY):
    """Load dictionary into a list and return list"""
    list = []
    f = open(DICTIONARY, 'r')
    for x in f:
        x = x.strip('\n')
        list.append(x)
    f.close()
    return list
    # pass

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    try:
        wordvalue = 0
        for g in word:
            for h in g:
                # print(g, h)
                x = LETTER_SCORES[h.upper()]
                wordvalue += x
    except Exception as e:
        print('Error found', e)
    return wordvalue
    # pass

def max_word_value(list=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # words = []
    if list == DICTIONARY:
        list = load_words(DICTIONARY)
    values = []
    for x in list:
        values.append(calc_word_value(x))

    # print(max(values))
    # print(values.index(max(values)))
    # print(list[values.index(max(values))])
    max_value = list[values.index(max(values))]
    return max_value
    # pass

if __name__ == "__main__":
    pass # run unittests to validate
