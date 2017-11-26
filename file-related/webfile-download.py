'''
quick script test to download files and store the content
'''

import requests, os

print(os.getcwd())

url = 'http://www.textfiles.com/computers/accel.txt'  # update url accordingly
fileName = 'test'  # name the file to be written without the extension

downloadFile = requests.get(url)
writtenFile = '%s.txt' % fileName

if downloadFile.status_code == 200:
    print('File downloaded to the variable successfully')
else:
    print('File download error. Try again')

print('')
with open(writtenFile, 'wb') as f:
    for x in downloadFile.iter_content(1000):
        f.write(x)

with open(writtenFile, 'r') as f:
    tempStorage = f.read()

print(tempStorage)





