#! python3

# markdownlistgenerator.py - Converts clipboard rows of text to a Markdown list.

import sys, pyperclip, pprint

clipboardIn = pyperclip.paste()

listItems = clipboardIn.split('\n')
listItems = [x.strip(' ').strip('\t') for x in listItems]

for i in range(len(listItems)):
		listItems[i] = '* ' + listItems[i] # add star to each line

listItems = list(filter(('* ').__ne__, listItems)) # remove blank lines

clipboardOut = '\n'.join(listItems)

pyperclip.copy(clipboardOut)