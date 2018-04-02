'''
Script used to recursively go through a folder and search text files for a specific string of interest.
It then outputs the name (including full path) of the file and the number of times the word was found.
'''


def findstring():

    wordOfInterest = input('Enter the case-sensitive string you want to search for: ')
    startDirectory = input('Enter the full path to the root folder that you want to start your search in: ')

    import os

    file_hits_dict = {}
    file_hits_list = []

    for this_dir, dir_names, file_names in os.walk(startDirectory):
        for eachFile in file_names:
            fpath = os.path.join(this_dir, eachFile)
            try:
                with open(fpath, 'r') as inputfile:
                    count = 0  # reset count when opening new file
                    for line in inputfile:
                        words = line.split()
                        for word in words:
                            if word == wordOfInterest:
                                count += 1
            except UnicodeDecodeError:
                print(f"This utility won't work on the non-text file \"{fpath}\"")
            if count > 0:
                file_hits_dict[fpath] = count  # creating a dictionary of files and word count for sorting
    if len(file_hits_dict) > 0:
        for k, v in file_hits_dict.items():
            file_hits_list.append((v, k))
        file_hits_sorted = sorted(file_hits_list, reverse=True)
        print(f"\nFiles containing the word \"{wordOfInterest}\" sorted by number of times the word occurs --")
        for hit in file_hits_sorted:
            print(hit)
    else:
        print(f"no files were found containing the word \"{wordOfInterest}\"")


findstring()