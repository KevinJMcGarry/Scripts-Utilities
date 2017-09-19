import os, re, itertools

def cleanlines(filename, numoflines):
    print(filename)
    baseFileName = os.path.splitext(filename)[0]
    print(baseFileName)
    with open(filename, 'r') as inputfile:
        with open(baseFileName + '-fixed.log', 'w') as outputfile:
            for line in itertools.islice(inputfile, numoflines):
                cleanedLines = re.sub(r"[']", "", line)  # used "" to encapsulate the single quote we want to remove from source
                outputfile.write(cleanedLines)
