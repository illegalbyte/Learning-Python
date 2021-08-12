#! python3

from pathlib import Path
import pprint as pp
import pyinputplus as pyip

workingDirectory = Path.cwd()


def findkeyword(searchterm, glob, directory):
    files = {}
    directory = Path(directory)
    for file in list(directory.glob(str(glob))):
        currentFile = open(file, "r")
        lineIndex = 0
        linesItemWasFound = []
        for line in currentFile:
            lineIndex += 1
            if searchterm in line:
                linesItemWasFound.append(lineIndex)
        if linesItemWasFound != []:
            files[str(file)] = linesItemWasFound
    return files

searchTerm = pyip.inputStr('Text to search for: ')
directoryToSearch = pyip.inputFilepath('Directory to search: ', mustExist=True)
globmatch = pyip.inputStr("Enter a glob for filetype: ")

# pp.pprint(findkeyword(searchTerm,globmatch ,directoryToSearch ))
for filePath, lines in findkeyword(searchTerm, globmatch, directoryToSearch).items():
    print(filePath +":      [", end='')
    
    for line in lines:
        if line != lines[-1]:
            print(str(line) + ", ", end='')
        else:
            print(str(line), end='')
    print(']')

