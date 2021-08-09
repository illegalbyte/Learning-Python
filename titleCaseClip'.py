#! python3

import sys
import pyperclip


def capitalise(word):
    return str(word[0].upper()) + str(word[1:])


def titlecase(string):
    listItems = string.split()

    for i, word in enumerate(listItems):
        if i == 0:
            listItems[0] = capitalise(listItems[0])
        elif word in ["and", "as", "but", "or", "if", "nor", "or", "so", "yet", 'a', 'an', 'the', 'as', 'at', 'by', 'for', 'in', 'of', 'off', 'on', 'per', 'to', 'up', 'via']:
            continue
        else:
            listItems[i] = capitalise(listItems[i])
    return(' '.join(listItems))


clipboardIn = pyperclip.paste()


print(titlecase('eve\'s big cat has been arrested for catnapping, cat burglary, and extortion.'))

pyperclip.copy(titlecase(clipboardIn))
