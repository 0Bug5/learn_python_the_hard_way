def break_words(stuff):
    '''This function will break up words for us'''
    # Wann layin zai mana spliting words dn n kamar haka " 'All', 'good', 'thing', etc.."
    words = stuff.split(' ')
    return words

# AIkin wnn fnx dn shine yayi mana sorting Words | Sentence.
def sort_words(words):
    '''Sort the words.'''
    return sorted(words)

# Wnn zae cire mana first word.
def print_first_word(words):
    '''Prints the first word after popping it off.'''
    word = words.pop(0)
    print(word)

# Wnn zae cire mana last word.
def print_last_word(words):
    '''Prints the last word after popping it off.'''
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    '''Takes in a full sentence and returns the sorted words.'''
    # Munyi storing fnx mai suna break_words(sentence) ciki variable 'words'.
    words = break_words(sentence)
    # Wnn zae mana sorting words dn na ta hanyar kiran sort_words(words) fnx.
    return sort_words(words)

def print_first_and_last(sentence):
    '''Print the first and last word of the sentence.'''
    # Munyi storing fnx mai suna break_words(sentence) ciki variable 'words'.
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    '''Sorts the words then prints the first and last one.'''
    words =  sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)