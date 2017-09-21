'''
	Connor Finley
	Advanced Python
	Assignment 3: Files, strings, and functions
	Madlibs
	Sep. 14, 2017
'''


def madlibs(inputname, outputname):
	adjective = input("Enter an adjective: ")
	noun1 = input("Enter an noun: ")
	verb = input("Enter an verb: ")
	noun2 = input("Enter an noun: ")

	f = open(inputname, 'r')
	content = f.read()
	f.close()

	content = content.replace("ADJECTIVE", adjective)
	content = content.replace("NOUN", noun1, 1)
	content = content.replace("VERB", verb)
	content = content.replace("NOUN", noun2)
	print("\n", content)

	with open(outputname, 'w') as o:
		o.write(content)
