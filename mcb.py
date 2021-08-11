#! python3
# mcb.pyw - Saves and loads text to the clipboard. 
# Usage: mcb.pyw save <keyword> # Saves Clipboard as your keyword
#        mcb.pyw <keyword> # loads keyword 
#        mcb.pyw list # lists all keyword shortcuts

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save Clipboard Content 
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List Keywords or load keyword content to clipboard
    if sys.argv[1].lower() == 'list':
        for key in mcbShelf.keys():
            print(str(list(mcbShelf.keys()).index(key)) + key)
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])





mcbShelf.close()
