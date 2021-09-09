#! python3

import sys
import random
import time
import bext

# CONSTANTS
WIDTH, HEIGHT = bext.size()
	# Can't print to the last column on Windows without it adding a new line
	# automatically, so reduce by one
WIDTH -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2

COLOURS = ['red','green','yellow','blue','magenta','cyan','white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_LEFT  = 'dl'
DOWN_RIGHT = 'dr'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)	

# Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
	bext.clear()

	# Generate some logos:
	logos = []
	for i in range(NUMBER_OF_LOGOS):
		logos.append(
			{COLOR: random.choice(COLOURS),
			X: random.randint(1, WIDTH - 4),
			Y: random.randint(1, HEIGHT - 4),
			DIR: random.choice(DIRECTIONS)
			}
		)
		if logos[-1][X] % 2 == 1:
			# make sure X is even so it can hit the corner
			logos[-1][X] -= 1
