# LabInventory

# Cron job set for daily to get inventory.
# Files will be archived once a month on 25th 
00 20 * * * ./Ankit/LabInventory/getLabInv.sh
00 19 25 * * ./Ankit/LabInventory/moveArchive.sh

# Below is executed from cron to execute python script
colt123@colt123:~/Ankit/LabInventory$ more getLabInv.sh
#!/bin/sh
python3 /home/colt123/Ankit/LabInventory/LabInvCisco.py
python3 /home/colt123/Ankit/LabInventory/LabInvAccedian.py

LabInvCisco.py      =>  For Cisco/AR devices
LabInvAccedian.py   =>  For Accedian devices