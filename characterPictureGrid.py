# ADAPTED FROM https://automatetheboringstuff.com/2e/chapter4/

grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]
# grid[x][y]

row = 9
column = 6

# for y in range(len(grid)): # where y is the y coordinate, and works as an index
# 	for x in range(len(grid[0][0])): # where x is the x coordinate, and works as an index
# 		print(grid[x][y], end='')
# 	print()

for y in range(column):
	for x in range(row):
		print( grid[x][y], end='' )
	print()
