# Script to reorder/swap every fourth and fifth line in the file

with open('pathToFile', 'r') as inputfile:
    with open('pathToFile', 'a') as outputfile:
        lines = []
        for line in inputfile:
            lines.append(line)
            if len(lines) == 5:  # writing the re-ordered lines to a new file
                outputfile.write(lines[0] + lines[1] + lines[2] + lines[4] + line[3])
                lines = []  # flushing the array to repopulate with next 5 lines
        if len(lines) > 0:  # conditional for lines left over
            linesLeft = len(lines)
            for i in range(linesLeft):
                outputfile.write(lines[i])