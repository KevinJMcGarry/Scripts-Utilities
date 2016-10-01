import requests, os

os.getcwd()

accelFile = requests.get('http://www.textfiles.com/computers/accel.txt')

if accelFile.status_code == 200:
    print('File downloaded to the variable successfully')
else:
    print('File download error. Try again')

print('')
with open('./Accel.txt', 'wb') as f:
    for x in accelFile.iter_content(1000):
        f.write(x)

with open('./Accel.txt', 'r') as f:
    blub = f.read()

print(blub)
