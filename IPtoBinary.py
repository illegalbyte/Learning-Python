#! python3

import pyinputplus as pyip
from textwrap import wrap

decimal_ip = pyip.inputStr("ENTER A DECIMAL NUMBER IP [EG: 127.0.0.1]: ")

decimal_numbers = decimal_ip.split('.')

#	128	64	32	16	8	4	2	1	
#	  1  2   3   4  5   6   7  8 
binaryPositionValue = [128, 64, 32, 16, 8, 4, 2, 1]


# for each number [127] in the list decimal_ append the binary

	# for each binaryPosition
		# 1: check if < binaryposition:
			# write 0 
		# 2: else: 
			# write 1
			# subtract number from position value
			#change decimal number to = the result of the subtraction


def Convert_IP(decimal_numbers: str) -> str:
	Binary = ''
	# loops over each '127' and '0' and '1' values in the IP:
	for decimalNumber in decimal_numbers:
		# loops over each 
			n = int(decimalNumber)
			binary_value = ''
			for binarypositionvalue in binaryPositionValue:
				if n < binarypositionvalue:
					binary_value += '0'
				else:
					binary_value += '1'
					n -= binarypositionvalue

			Binary += binary_value 
	return Binary

def ConvertBinary(binaryIP):
	bytes = wrap(binaryIP, 8)
	# for each byte:
	fulldecimalIP = []
	for byte in bytes:
		decimal = 0
		#for each bit in the byte * by the binary position value 
		for i, bit in enumerate(byte):
			decimal += int(bit) * binaryPositionValue[i]
		fulldecimalIP.append(decimal)
	return '.'.join(map(str, fulldecimalIP))

print("BINARY OUTPUT: ", end='')
print(Convert_IP(decimal_numbers))
print("IP OUTPUT: ", end='')
print(ConvertBinary(Convert_IP(decimal_numbers)))
