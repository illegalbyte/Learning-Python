tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Lewis', 'Neha', 'Daniel', 'Alisha'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(table):
	colWidths = [0] * len(table)
	
	for i, value in enumerate(table):
		colWidths[i] = len(max(table[i])) + 5

	for i, value in enumerate(table[0]):
		print(table[0][i].ljust(colWidths[0]) + table[1][i].ljust(colWidths[1]) + table[2][i].ljust(colWidths[2]))


printTable(tableData)