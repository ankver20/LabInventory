# device IP is taken from InventoryDevice.txt
# 11 Mar 2020 : try and except added
# 02 May 2020 : add system path

from netmiko import ConnectHandler
import time, re, sys
import socket, difflib
from time import gmtime, strftime
import getpass

file_path = os.path.dirname(os.path.realpath(__file__))

def netmiko_ssh():
    deviceIP = DeviceList()
    print(deviceIP)
    for i in range (len(deviceIP)):
        try:
            dp = deviceIP[i]

            net_connect = ConnectHandler(device_type='cisco_xr', ip= dp, username='averma2', password='Ank#2018', port = 22)
            output = net_connect.send_command_expect("ter len 0", delay_factor=2)
            print(output)
            output = net_connect.send_command_expect("sh inventory", delay_factor=2)
            print('\n'+dp+'####')
            print(output)
            c = output
            createLog('\n'+dp+'####')
            createLog(c)
            time.sleep(1)
            InvetoryCheck(c,dp)

        except Exception as e:
            c = str(e)
            print('\n'+dp+'####')
            print(c)
            createLog('\n'+dp+'####')
            createLog(c)



# Raw log is created
def createLog(c):
    LocalTime= strftime("%d%m%Y", gmtime())
    f = open(file_path + '/CiscoInv/InventoryRaw-' + LocalTime + '.txt', 'a')
    f.write(c)
    #f.write('\n\n')
    f.close()

# read inventory device details from txt file
def DeviceList():
    f = open(file_path + '/InventoryDevice.txt','r')
    f1 = f.readlines()
    return f1

# get interface and serial number
def InvetoryCheck(c,dp):
    interface = re.findall('NAME: (\".*?\")',c)
    serial = re.findall('SN: \w+',c)
    print (interface)
    print (serial)
    print(len(interface))
    print(len(serial))
    createLogInventory(interface, serial,dp)

# create log in the required format
def createLogInventory(interface, serial,dp):
    LocalTime= strftime("%d%m%Y", gmtime())
    dp = dp.rstrip('\n')
    f = open(file_path + '/CiscoInv/Inventory-' + LocalTime + '.txt', 'a')
    for i in range(len(interface)):
        f.write(dp + ';' + interface[i] + ';'  + serial[i])
        f.write('\n')
    f.close()


netmiko_ssh()

