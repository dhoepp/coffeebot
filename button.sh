#!/bin/bash

pkill -f 'python3.*pots.py'
python3 /home/pi/pots.py > /dev/null 2>&1 & disown

