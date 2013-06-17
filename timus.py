from sys import argv
import os

scriptName, command, argument = argv

if command == 'create':
	os.makedirs("Timus/%s/" %argument)
	open("Timus/%s/solution.py" %argument, 'w').close()
