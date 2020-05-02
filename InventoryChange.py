# Get inventory (SFP Serial Number) details in Lab

import paramiko, time, re, sys
import socket, difflib
from time import gmtime, strftime
import getpass


def InventoryChange():

    f1 = str(input('Enter OLD Inventory File Name= '))
    f2 = str(input('Enter TODAYs Inventory File Name= '))

    f11 = open(f1, 'r')
    f13 = f11.readlines()
    
    f22 = open(f2, 'r')
    f23 = f22.readlines()

    # Check Difference
    for line in difflib.unified_diff(f13, f23, lineterm="",n=0):
        #print(line)
        if ('+' in line):
            if ('@' in line):
                continue
            else:
                print(line)
                InventoryChangeLog(line)
        elif ('-' in line):
            if ('@' in line):
                continue
            else:
                print(line)
                InventoryChangeLog(line)

def InventoryChangeLog(line):
    LocalTime= strftime("%d%m%Y", gmtime())
    
    f33 = open('InventoryChange-' + LocalTime + '.txt', 'a')
    f33.write(line + '\n')
    f33.close()

InventoryChange()
