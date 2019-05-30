'''
Cisco IOS Utility that pulls ios version info and stores it in a csv file
'''

from getpass import getpass
import netmiko
import re
import os

def make_connection (ipaddress, username, password):
    return netmiko.ConnectHandler(device_type='cisco_ios', ip=ipaddress, username=username, password=password)

def IPAddressCarver(input):
    return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

def getIPAddresses(file_name):
    with open(file_name, 'r') as inputFile:
        for line in inputFile:
            found_ips = IPAddressCarver(line)
            ipAddressList.extend(found_ips)

ipAddressList = []

file_name = input('Enter the name of the file you want to search for IP Addresses: ')
getIPAddresses(file_name)

# prompt for username and password to log into devices
username = input('Username: ')
password = getpass()

with open('results.csv', 'w') as inputFile2:
    for ipaddress in ipAddressList:
        print('Connecting to device at {}'.format(ipaddress))
        net_connect = make_connection(ipaddress, username, password)
        output = net_connect.send_command_expect('show ver | i .bin')
        for each_word in output.split(" "):
            if ".bin" in each_word:
                version = each_word
                results = ipaddress + ", " + version + ", " + "\n"
                print('Writing ' + results.strip("\n") + 'to the file results.csv')
        inputFile2.write(results)
