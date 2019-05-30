'''
quick script (not using functions) to create a sorted list of ip addresses used in a file
''' 

import os, re

ipAddressList = []
ipAddressDict = {}
ipAddressList2 = []

os.chdir('../../Downloads')  # change to appropriate folder or enter full path when opening
print(os.getcwd())
with open('./fankey.log', 'r') as inputfile:  # adjust name accordingly
    for line in inputfile:
        foundIPs = re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', line)
        ipAddressList.extend(foundIPs)  # extending the list with each ip found. append would add list inside of the list.

# print(ipAddressList)


for element in ipAddressList:
    if element not in ipAddressDict:
        ipAddressDict[element] = 1
    else:
        ipAddressDict[element] = ipAddressDict[element] + 1

print(ipAddressDict)
for k,v in ipAddressDict.items():
    ipAddressList2.append((v,k))
print(ipAddressList2.sort())  # sorted list of ip addresses in descending order