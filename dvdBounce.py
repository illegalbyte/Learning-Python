#! python3

import sys
import random
import time
import bext
import pyinputplus as pyip

# CONSTANTS
WIDTH, HEIGHT = bext.size()
	# Can't print to the last column on Windows without it adding a new line
	# automatically, so reduce by one
WIDTH -= 1
NUMBER_OF_LOGOS = 100
PAUSE_AMOUNT = 0.2

COLOURS = ['red','green','yellow','blue','magenta','cyan','white']
LOGO = 'Novio'
LOGO_LENGTH = len(LOGO) + 2

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_LEFT  = 'dl'
DOWN_RIGHT = 'dr'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)	

# Key names for logo dictionaries
COLOUR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
	bext.clear()

	LOGO = pyip.inputStr("ENTER TEXT TO BOUNCE AROUND TERMINAL\n> ")
	# Generate some logos:
	logos = []
	for i in range(NUMBER_OF_LOGOS):
		logos.append(
			{COLOUR: random.choice(COLOURS),
			X: random.randint(1, WIDTH - LOGO_LENGTH + 1),
			Y: random.randint(1, HEIGHT - LOGO_LENGTH + 1),
			DIR: random.choice(DIRECTIONS)
			}
		)
		if logos[-1][X] % 2 == 1:
			# make sure X is even so it can hit the corner
			logos[-1][X] -= 1

	# count corner bounces
	cornerBounces = 0
	# Main program loop
	while True: 
		for logo in logos:
			# Erase logo's current location:
			bext.goto(logo[X], logo[Y])
			print(' '*LOGO_LENGTH, end='')

			originalDirection = logo[DIR]

			# see if the logo bounces off the corners 
			if logo[X] == 0 and logo[Y] == 0:
				logo[DIR] = DOWN_RIGHT
				cornerBounces += 1
			elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
				logo[DIR] = UP_RIGHT
				cornerBounces += 1
			elif logo[X] == WIDTH - LOGO_LENGTH and logo[Y] == 0:
				logo[DIR] = DOWN_LEFT
				cornerBounces += 1
			elif logo[X] == WIDTH - LOGO_LENGTH and logo[Y] == HEIGHT - 1:
				logo[DIR] = UP_LEFT
				cornerBounces += 1
			# see if logo bounces off left edge
			elif logo[X] == 0 and logo[DIR] == UP_LEFT:
				logo[DIR] = UP_RIGHT
			elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
				logo[DIR] = DOWN_RIGHT
			# see if logo bounces off right edge
			elif logo[X] == WIDTH - LOGO_LENGTH and logo[DIR] == UP_RIGHT:
				logo[DIR] = UP_LEFT
			elif logo[X] == WIDTH - LOGO_LENGTH and logo[DIR] == DOWN_RIGHT:
				logo[DIR] = DOWN_LEFT
			# if logo bounces off the top edge
			elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
				logo[DIR] = DOWN_LEFT
			elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
				logo[DIR] = DOWN_RIGHT
			# if logo bounces off bottom edge 
			elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
				logo[DIR] = UP_LEFT
			elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
				logo[DIR] = UP_RIGHT

			# Change logo colour when bounced
			if logo[DIR] != originalDirection:
				logo[COLOUR] = random.choice(COLOURS)

			# Move the logo 
			#	 (X moved by 2 bc the terminal characters are 
			#	 twice are 2x as tall as they are wide )
			if logo[DIR] == UP_RIGHT:
				logo[X] += 2
				logo[Y] -= 1
			elif logo[DIR] == UP_LEFT:
				logo[X] -= 2
				logo[Y] -= 1
			elif logo[DIR] == DOWN_RIGHT:
				logo[X] += 2
				logo[Y] += 1
			elif logo[DIR] == DOWN_LEFT:
				logo[X] -= 2
				logo[Y] += 1

			# Display number of corner bounces
			bext.goto(5, 0)
			bext.fg('white')
			print(f'Corner Bounces: {cornerBounces}', end='')

		# Draw logos at their new location
		for logo in logos:
			bext.goto(logo[X], logo[Y])
			bext.fg(logo[COLOUR])
			print(f'{LOGO}', end='')

		bext.goto(0, 0)

		# Required for bext
		sys.stdout.flush()
		# Pause for animation smoothness
		time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
	try:
		main()
	# Handle Ctr-C to exit:
	except KeyboardInterrupt:
		print()
		print('Bouncing logo animation, adapted from Al-Sweigart\'s Book of Python Projects (https://inventwithpython.com).')
		sys.exit() 
