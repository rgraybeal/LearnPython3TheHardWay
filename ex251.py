

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    print(">>Break_words function call")
    return words

def print_first_word(words):
    """prints the first wod after popping it off."""
    word = words.pop(0)
    print(" >>First_word function output")
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(" >>Last_word function output")
    print(word)
def print_first_and_last(sentence):
    """Prints the first and last wrods of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
