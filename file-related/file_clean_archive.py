'''
script to take user input, scan folder, iterating over the first n lines of each file, applying
regex substitution, writing cleaned lines to a new file in a separate folder and finally taring
up the original files and storing them in a separate source folder with a date/timestamp for the name
'''

import os, re, datetime, tarfile

def cleanfiles(folder, numoflines):
    print(os.getcwd())
    counter = 1
    cleanedfolder = "cleanedfiles"  # specifying folder location of where to store the modified files
    if not os.path.exists(os.path.join(folder, cleanedfolder)):
        os.mkdir(os.path.join(folder, cleanedfolder))  # makes a folder called 'cleanedfiles' under folder path
    for eachfile in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, eachfile)):  # only work on files, not folders
            print(eachfile)
            with open(eachfile, 'r') as inputfile:
                #with open(os.path.join(folder, cleanedfolder, eachfile + '.new'), 'w') as outputfile:
                with open(os.path.join(folder, cleanedfolder, (datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S'))
                        + ".txt"), 'w') as outputfile:
                    for line in inputfile:
                        if counter > 5:
                            break
                        re.sub("chaka", "foo", line)  # adjust strings to substitute accordingly
                        outputfile.write(line)
                        counter += 1