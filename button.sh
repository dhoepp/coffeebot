#!/bin/bash

#kill existing pots.py script to prevent overlapping notifications
pkill -f 'python3.*pots.py'
#initiate new pots.py and disown
python3 /home/pi/pots.py > /dev/null 2>&1 & disown

