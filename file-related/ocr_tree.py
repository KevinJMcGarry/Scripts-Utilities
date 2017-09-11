'''
Utility that leverages the ocrmypdf library to auto-ocr all pdfs in all folders and subfolders.
note that ocrmypdf must be installed on the local computer prior to running this script
https://pypi.python.org/pypi/ocrmypdf

mac users can run --
brew tap jbarlow83/ocrmypdf
brew install ocrmypdf

'''

#!/usr/bin/env python

import logging
import os
import subprocess
import sys
import time

print(os.getcwd())

scriptDir = os.path.dirname(os.path.realpath(__file__))
print(scriptDir + '/ocr_tree.py: Start')

time.sleep(5)

if len(sys.argv) > 1:  # first parameter option to specify is path of folder to 'walk'
    startDirectory = sys.argv[1]
else:
    startDirectory = '.'

if len(sys.argv) > 2:  # second parameter option could be path to a log file
    logFile = sys.argv[2]
else:
    logFile = scriptDir + '/ocr_tree.log'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename=logFile, filemode='w')

for directoryName, subdirectoryList, fileList in os.walk(startDirectory):
    print(directoryName, subdirectoryList, fileList)
    logging.info('\n')
    logging.info(directoryName + '\n')
    # os.chdir(directoryName)
    for eachFileName in fileList:
        print(eachFileName)
        fileExtension = os.path.splitext(eachFileName)[1]  # make sure this is splitting on last .
        if fileExtension == '.pdf':
            baseFileName = os.path.splitext(eachFileName)[0]
            print(baseFileName)
            fullPath = directoryName + '/' + eachFileName
            print(fullPath)
            ocrCommand = [r"ocrmypdf",  "--deskew", os.path.join(directoryName, eachFileName),
                          os.path.join(directoryName, baseFileName + '-ocr.pdf')]  # os.path.join to traverse all subdirs
            logging.info(ocrCommand)
            proc = subprocess.Popen(ocrCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = str(proc.stdout.read())  # needed to cast this to string as subprocess returns bytes objects
            # print(result)
            if 'page already has text' in result:  # checking to see if file has already been ocr'd
                result = 'Skipped document because it already contains searchable text'
                print(result)
            else:
                print('OCR complete')
            logging.info(result)
