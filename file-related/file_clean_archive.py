'''
script to take user input, scan folder, iterating over the first n lines of each file, applying
regex substitution, writing cleaned lines to a new file in a separate folder and finally taring
up the original files and storing them in a separate source folder with a date/timestamp for the name

Usage:

python3 file_clean_archive
'''

import os, re, datetime, gzip, shutil, sys

if len(sys.argv) < 3:
    print("\n*****************************************************************************")
    print("you must furnish the folder path and number of lines arguments")
    print("example - python3 file_clean_archive.py \"/Users/kevinmcgarry/foldername\" 7")
    print("be sure to use quotes around the full folder path")
    print("*****************************************************************************\n")
    exit()
else:
    folder = sys.argv[1]
    numoflines = int(sys.argv[2])  # casting to int for counter operation

print("\nprocessing file in folder {} ... \n".format(folder))


def cleanfiles(folder, numoflines):

    cleanedfolder = "cleanedfiles"  # specifying folder location of where to store the modified files
    archivedfolder = "archives"
    cleanedFolderPath = os.path.join(folder, cleanedfolder)
    archivedFolderPath = os.path.join(folder, archivedfolder)

    if not os.path.exists(cleanedFolderPath):
        os.mkdir(cleanedFolderPath)  # makes a folder called 'cleanedfiles' under specified folder path
    for eachfile in os.listdir(folder):
        eachFilePath = os.path.join(folder, eachfile)
        counter = 1
        if eachfile.endswith("DS_Store"):
            continue  # skip mac created .DS_Store files
        if os.path.isfile(eachFilePath):  # only work on files, not folders
            print('processing file ... {} ...'.format(eachfile))
            with open(os.path.join(eachFilePath), 'r') as inputfile:
                with open(os.path.join(cleanedFolderPath, eachfile + "_" +
                        (datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')) + ".txt"), 'w') as outputfile:
                    for line in inputfile:
                        if counter > numoflines:  # only working with the first n lines of each file
                            break
                        re.sub("chaka", "foo", line)  # adjust strings to substitute accordingly
                        outputfile.write(line)
                        counter += 1
            if not os.path.exists(archivedFolderPath):
                os.mkdir(archivedFolderPath)
            zip_file_name = eachfile + '.zip'
            zip_file_path = os.path.join(archivedFolderPath, zip_file_name)
            with open(os.path.join(eachFilePath), 'rb') as f_in:
                with gzip.open(os.path.join(archivedFolderPath, eachfile + '.gz'), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(os.path.join(eachFilePath))  # delete the original files after archive complete

cleanfiles(folder, numoflines)
