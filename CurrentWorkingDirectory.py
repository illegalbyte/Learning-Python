#! python3

from pathlib import Path
import os, pprint

def getMaxString(lst):
    return max(lst, key=len)

workingDirectory = Path.cwd()
kilobyte = 1024


print(workingDirectory)
print(f'Current Directory Size: {(os.path.getsize(workingDirectory)/kilobyte)} Kilobytes')


################################
# using a list to store working directory names: (deprecated)
################################ 
''' 
CWDlist = os.listdir(workingDirectory)

maxFileCharacterWidth = len(getMaxString(CWDlist))


for file in CWDlist:
    fileSize = round(os.path.getsize(file) / kilobyte,2)
    print(f'{file}'.ljust(maxFileCharacterWidth+2) + f'{fileSize}'.rjust(6))
'''

################################
# using a dictionary to store working directory names and size:
################################
CWD = Path.cwd()
print(CWD)
CWDdict = {}

# for all files in working directory:
# assign filename as key and value as the filesize in kilobytes
for file in os.listdir(workingDirectory):
    CWDdict[file] = round(os.path.getsize(file) / kilobyte, 2)

maxFileCharacterWidth2 = len(getMaxString(CWDdict.keys())) + 3
maxFilesizeCharacterWidth = len(getMaxString(CWDdict.items())) + 10

for file, size in CWDdict.items():
    print(f'{file}'.ljust(maxFileCharacterWidth2) + 
        f'{size} KB'.rjust(maxFilesizeCharacterWidth))

