# https://automatetheboringstuff.com/2e/chapter6/
"""
A multiline string in Python begins and ends with either three single quotes or three double quotes. 
Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string. 
Python’s indentation rules for blocks do not apply to lines inside a multiline string.

They can also be used for multiline comments like this. 
"""

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

"""
Python 3.6 introduced f-strings, which is similar to string interpolation except 
hat braces are used instead of %s, with the expressions placed directly inside the braces. 
Like raw strings, f-strings have an f prefix before the starting quotation mark. 
Enter the following into the interactive shell:
"""

name = 'Lewis Gentle'
age = 22
year = 2021
# remember to put the f prefix before the opening quotation
print(f"My name is {name}, it's {year} and I'm {age} years old.")

"""
METHODS:
isalpha() Returns True if the string consists only 
	of letters and isn’t blank
isalnum() Returns True if the string consists only 
	of letters and numbers and is not blank
isdecimal() Returns True if the string consists only 
	of numeric characters and is not blank
isspace() Returns True if the string consists only 
	of spaces, tabs, and newlines and is not blank
istitle() Returns True if the string consists only 
	of words that begin with an uppercase letter followed by only lowercase letters

startswith()
endswith()

"""

# join()
string = ['cat', 'novio', 'peace', 'tech']
print(', '.join(string) + " [[[VS REGULAR PRINT:]]] ", end='' )
print(string)

#split(): splits up a string into individual words, or split based on any delimeter passed
string2 = 'Happy Novio, Happy Life'
print(string2.split()) # => ['Happy', 'Novio,', 'Happy', 'Life']
print(string2.split(', ')) # => ['Happy Novio', 'Happy Life']

# partition() method: 
'Hello, world!'.partition('w') #=> ('Hello, ', 'w', 'orld!')

# rjust(), ljust(), and center()


print('Hello!'.rjust(10))
print(''.center(16,'🌈'))
print(' Hello '.center(20, '🌈'))
print(''.center(16,'🌈'))




