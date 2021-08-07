#! python3

# clipboardResponse.py - A Multi-Clipboard Application
# Chapter project for https://automatetheboringstuff.com/2e/chapter6/

# modules
import pyperclip, sys


RESPONSE = {
	'agree': """Sounds great. Let's do that""",
	'busy': """I'm pretty busy, let's try later this week.""",
	'contract': """The hourly rate starts at $600, depending on the complexity of the job."""
}

if len(sys.argv) < 2:
	print('Usage: python3 clipboardResponse.py [shortcut\'s nickname] - copy phrase text')
	sys.exit(0)

keyPhrase = sys.argv[1] # first command line arg is keyPhrase

if keyPhrase in RESPONSE:
	pyperclip.copy(RESPONSE[keyPhrase])
	print(f'Text for \'{keyPhrase}\' copied to clipboard.')
else:
	print(f'There is no text for {keyPhrase}')