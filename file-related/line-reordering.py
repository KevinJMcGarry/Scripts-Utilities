# Script to reorder every fourth line with every fifth line

with open('pathToFile', 'r') as inputfile:
    with open('pathToFile', 'a') as outputfile:
        lines = []
        for line in inputfile:
            lines.append(line)
            if len(lines) == 5:  # writing the re-ordered lines to a new file
                outputfile.write(lines[0] + lines[1] + lines[2] + lines[3] + line[5] + line[4])
                lines = []  # flushing the array to repopulate with next 3 lines
        if len(lines) > 0:  # conditional for lines left over
            linesLeft = len(lines)
            for i in range(linesLeft):
                outputfile.write(lines[i])