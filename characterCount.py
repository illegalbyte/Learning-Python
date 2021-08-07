# Learning dictionaries 
# Derived from: https://automatetheboringstuff.com/2e/chapter5/

#import prettyprint
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

# counts all the characters
for character in message:
	count.setdefault(character,0)
	count[character] += 1

#how to print the dictionary in a pretty way using pprint
pprint.pprint(count)

#how to store a prettier version of the dictionary
prettyDictionary = pprint.pformat(count)

