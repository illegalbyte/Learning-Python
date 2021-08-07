# Exercise from https://automatetheboringstuff.com/2e/chapter5/ 

board = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop',
'1g': 'wknight', '1h': 'wrook','2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn',
'2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
'3g': '', '3h': '', '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
'7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
'8a': 'brook', '8b': 'bknight', '8c': 'bbishop' , '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop',
'8g': 'bknight','8h': 'brook'}

def validChessBoard(inputBoard):
	blackKing = 0 # only 1
	blackPieces = 0 # at most 16
	blackPawns = 0 # at most 8

	whiteKing = 0 # only 1
	whitePieces = 0 # at most 16
	whitePawns = 0 # at most 8

	# all pieces must be on a valid space 1a - 1h, 8a-8h 

	# count & check pieces
	for space in inputBoard.values():
		if space == 'bking':
			blackKing += 1
			if blackKing > 1:
				print('--- Board is Invalid ---')
				print('Exceeded number of Black Kings (1), you have '+ str(blackKing))
		if space == 'wking':
			whiteKing +=1
			if whiteKing > 1:
				print('--- Board is Invalid ---')
				print('Exceeded number of White Kings (1), you have '+ str(whiteKing))
		if space == 'bpawn':
			blackPawns +=1
			if blackPawns > 8:
				print('--- Board is Invalid ---')
				print('Exceeded number of Black Pawns (8), you have '+ str(blackPawns))
		if space == 'wpawn':
			whitePawns +=1
			if whitePawns > 8:
				print('--- Board is Invalid ---')
				print('Ex8ceeded number of White Pawns (8), you have '+ str(whitePawns))
		if space.startswith('w'):
			whitePieces +=1
			if whitePieces > 16:
				print('--- Board is Invalid ---')
				print('Exceeded number of White Pieces (16), you have '+ str(whitePieces))
		if space.startswith('b'):
			blackPieces +=1
			if blackPieces > 16:
				print('--- Board is Invalid ---')
				print('Exceeded number of Black Pieces (16), you have '+ str(blackPieces))

validChessBoard(board)

