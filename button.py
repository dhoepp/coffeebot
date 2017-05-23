from scapy.all import *
from time import sleep
import requests
import subprocess
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def arp_display(pkt):
  if pkt[ARP].pdst == '172.17.0.1':
    if pkt[ARP].hwsrc == '44:65:0d:45:fd:9c':
      print( "1")
      subprocess.call('/home/pi/button.sh')
      print("2")

print( sniff(prn=arp_display, filter="arp", store=0))
