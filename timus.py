from sys import argv
import os

scriptName, command, argument = argv

if command == 'create':
	dirName = "Timus/%s/" %argument
	os.makedirs(dirName)
	open("%ssolution.py" %dirName, 'w').close()	
	open("%sREADME.md" %dirName, 'w').close()
