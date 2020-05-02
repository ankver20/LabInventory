## History
# 22 Feb 2020 Created to fetch Accedian SFP/inventory details
# 23 Feb 2020 Try and Except added under for loop, so that if SSH fails on any device, program continues
# 02 May 2020 : add system path


# Device IP is taken from AccedianInventoryDevice.txt

from netmiko import ConnectHandler
import time, re, sys
import socket, difflib
from time import gmtime, strftime
import os

file_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    # Accedian username & PW for BLR Lab
    username = 'admin'
    pw = 'admin'
    deviceType = 'accedian'
    port = '22'

def accedian_sfp():
    deviceIP = DeviceList()
    print(deviceIP)
    for i in range(len(deviceIP)):
        dp = deviceIP[i]
        try:
            accedian_ssh(dp)

        except Exception as e:
            c = str(e)
            c = '\n'+str(dp)+' : '+c+'\n'
            print(c)
            createLog(c)
            time.sleep(1)

def accedian_ssh(dp):
    net_connect = ConnectHandler(device_type=deviceType, ip=dp, username=username, password=pw, port=port)

    output = net_connect.send_command_expect("sfp show status")   #get SFP details from accedian device
    print('\n'+dp+'####')
    print(output)
    c = output
    createLog('\n'+dp+'####')
    createLog(c)
    time.sleep(1)
    AccedianInvetoryCheck(c,dp)
    net_connect.disconnect()


# Raw log is created
def createLog(c):
    LocalTime= strftime("%d%m%Y", gmtime())
    f = open(file_path + '/AccedianInv/AccedianInventoryRaw-' + LocalTime + '.txt', 'a')
    f.write(c)
    #f.write('\n\n')
    f.close()

# read inventory device details from txt file
def DeviceList():
    f = open(file_path + '/AccedianInventoryDevice.txt','r')
    f1 = f.readlines()
    return f1

# get interface and serial number
def AccedianInvetoryCheck(c,dp):
    data = re.findall('Yes\s+(SFP-\d+)\s+(\S+)\s+(\S+)\s+(\d+\s+\S+)\s+(\d+\S+)',c)
    #print (data)
    createLogInventory(data, dp)

# create log in the required format
def createLogInventory(data, dp):
    LocalTime= strftime("%d%m%Y", gmtime())
    dp = dp.rstrip('\n')
    f = open(file_path + '/AccedianInv/AccedianInventory-' + LocalTime + '.txt', 'a')
    for i in range(len(data)):
        #Connector  Part number      Serial number     Wavelength    Speed#
        f.write(dp+';'+data[i][0]+';'+data[i][1]+';'+data[i][2]+';'+data[i][3]+';'+data[i][4])
        print(dp+';'+data[i][0]+';'+data[i][1]+';'+data[i][2]+';'+data[i][3]+';'+data[i][4])
        f.write('\n')        
    f.close()


accedian_sfp()

