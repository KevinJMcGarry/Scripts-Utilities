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

os.chdir('../../temp9/')
print(os.getcwd())

scriptDir = os.path.dirname(os.path.realpath(__file__))
print(scriptDir + '/ocr_tree.py: Start')

time.sleep(5)

if len(sys.argv) > 1:  # first parameter option to specify is path of folder to 'walk'. value assigned to startDirectory
    startDirectory = sys.argv[1]
else:
    startDirectory = '.'  # default directory to use if one isn't specified at runtime

if len(sys.argv) > 2:  # second parameter option could be path to a log file
    logFile = sys.argv[2]
else:
    logFile = scriptDir + '/ocr_tree.log'  # default log file to use if one isn't specified at runtime

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename=logFile, filemode='w')

for directoryName, subdirectoryList, fileList in os.walk(startDirectory):
    print(directoryName, subdirectoryList, fileList)
    time.sleep(5)
    logging.info('\n')
    logging.info(directoryName + '\n')
    for eachFileName in fileList:
        fileExtension = os.path.splitext(eachFileName)[1]  # make sure this is splitting on last .
        if eachFileName[-8:] == "-ocr.pdf":  # logic to skip previously ocr'd files
            print('The file "{}" has already been ocr\'d by ocrmypdf!!'.format(eachFileName))
            continue
        if fileExtension == '.pdf':
            baseFileName = os.path.splitext(eachFileName)[0]
            ocrCommand = [r"ocrmypdf",  "--deskew", os.path.join(directoryName, eachFileName),
                          os.path.join(directoryName, baseFileName + '-ocr.pdf')]  # os.path.join to traverse all subdirs
            logging.info(ocrCommand)
            proc = subprocess.Popen(ocrCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # stdout stored in proc
            # stdout data from the Popen 'ocrCommand' is stored in proc variable
            result = str(proc.stdout.read())  # needed to cast this to string as subprocess returns bytes objects
            # print(result)
            if 'page already has text' in result:  # checking to see if file has already been ocr'd
                result = 'Skipped the file "{}" because it already contains searchable text'.format(eachFileName)
                print(result)
            else:
                print('OCR of file "{}" complete'.format(eachFileName))
            logging.info(result)
