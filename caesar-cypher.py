try: 
	import pyinputplus
except ImportError:
	print('Missing dependencies: pyinputplus')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mode = pyinputplus.inputMenu(['Encrypt', 'Decrypt'], "\nWhat would you like to do?\n", lettered=True)

# ask for the cipher offset
maxKey = len(SYMBOLS) - 1
key = pyinputplus.inputInt(f"\nEnter a number between 1 and {maxKey} to {mode} your message with\n", min=1, max=maxKey)

message = pyinputplus.inputStr(f'Enter the message to {mode}\n> ')
message = message.upper()

translated = ''

# Encrypt/decrypt each symbol in the message: 
for symbol in message:
	if symbol in SYMBOLS:
		# get the encrypted / decrypted number for this symbol
		num = SYMBOLS.find(symbol)
		if mode == 'Encrypt':
			num = num + key
		elif mode == 'Decrypt':
			num = num - key
		
		# handle the wrap around if num is larger than the length of 
		# SYMBOLD or less than 0 
		if num >= len(SYMBOLS):
			num = num - len(SYMBOLS)
		elif num < 0:
			num = num + len(SYMBOLS)

		# Add encrypted / decrypted number's symbol to translated
		translated += SYMBOLS[num]
	else:
		# just add the symbol without encrypting/decrypting
		translated += symbol

# print translated message 
print(f'YOUR MESSAGE {mode.upper()}ED:\n{translated}')