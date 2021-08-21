#! python3
# bitmapPrinter.py – prints a predefined bitmap image using a string input 

import sys
import pyinputplus as pyip

# 68 period wide ascii image
BITMAP_WIDTH = 68
BITMAP_IMAGE = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''

message = pyip.inputStr("Enter a message to print the bitmap with: ")

# loop over each bitmap in image
for line in BITMAP_IMAGE.splitlines():
	# loop over each character in bitmap image
	for i, bit in enumerate(line):
		if bit == ' ':
			print(' ', end='')
		else:
			print(message[i % len(message)], end='')
	print()