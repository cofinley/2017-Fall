'''
	Connor Finley
	Advanced Python
	Assignment 3: Files, strings, and functions
	Table Printer
	Sep. 14, 2017
'''


def printTable(L):
	widths = []
	for l in L:
		width = len(max(l, key=len))
		widths.append(width)

	table = list(zip(L[0], *L[1:]))

	for row in table:
		for i, column in enumerate(row):
			print(column.rjust(widths[i]), end=" ")
		print()

tableData = [
	['apples', 'oranges', 'cherries', 'banana'],              
	['Alice', 'Bob', 'Carol', 'David'],              
	['dogs', 'cats', 'moose', 'goose']
] 
printTable(tableData)
