# Script to reorder/swap every fourth and fifth line in the file

'''
to do
- turn into function
- add arguments for path to source and destination file
'''

lines = []  # create empty list

with open('pathToFile', 'r') as inputfile:
    with open('pathToFile', 'a') as outputfile:  # writing the re-ordered lines to a new file
        for line in inputfile:
            lines.append(line)
            if len(lines) == 5:
                outputfile.write(lines[0] + lines[1] + lines[2] + lines[4] + line[3])
                lines = []  # flushing the array to repopulate with next 5 lines
        if len(lines) > 0:  # conditional for lines left over that don't add up to 5 lines
            leftOverLines = len(lines)
            for i in range(leftOverLines):
                outputfile.write(lines[i])