#####
#script watching for button press
from scapy.all import *
from time import sleep
import requests
import subprocess
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def arp_display(pkt):
  #runs a tcpdump on the network looking for the default gateway (this prevents double button pressing)
  if pkt[ARP].pdst == '172.17.0.1':
    #runs a tcpdump on the network looking for instances of the MAC address of the amazon button
    if pkt[ARP].hwsrc == '44:65:0d:45:fd:9c':
      #print( "1") #used for testing
      subprocess.call('/home/pi/button.sh') #initiates button.sh when the button is pressed
      #print("2") #used for testing

print( sniff(prn=arp_display, filter="arp", store=0))
