#!/bin/bash
#run this script to initiate waiting for button press
sudo python3 /home/pi/button.py > /dev/null 2>&1 & disown
