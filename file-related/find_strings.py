'''
Script used to recursively go through a folder and search each file for a specific string of interest.
It then outputs in what file (and the number of times in that file) that the string was found.
Going to update with exception handling.
'''


def findstring():

    wordOfInterest = input('Enter the case-sensitive string you want to search for: ')
    startDirectory = input('Enter the full path to the root folder that you want to start your search in: ')

    import os

    for this_dir, dir_names, file_names in os.walk(startDirectory):
        for eachFile in file_names:
            fpath = os.path.join(this_dir, eachFile)
            with open(fpath, 'rb') as inputfile:
                count = 0
                for line in inputfile:
                    if wordOfInterest in str(line):
                        count += 1
            if count > 0:
                print("found the word \'{}\' {} times in file \'{}\'".format(wordOfInterest, count, fpath))

findstring()