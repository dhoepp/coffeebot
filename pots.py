from scapy.all import *
from time import sleep
import requests
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def send_message1():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif", #this is the user image used inline with chat
    "text": "Coffee Started", 
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

def send_message2():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif", #this is the user image used inline with chat
    "text": ":coffee: Fresh Pots :coffee:",
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

def send_message3():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif", #this is the user image used inline with chat
    "text": ":alarm: WARNING! Coffee Pot Powering Off!! :alarm:",
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

send_message1() #Coffee Started
sleep(720) #wait 12 minutes for brew time
send_message2() #:coffee: Fresh Pots :coffee:
sleep(6480) #wait (2 hours - 12 minutes) for coffee pot to power off (change to 7200 if coffee pot starts timer after coffee is done)
send_message3() #:alarm: Coffee Pot Powering Off!! :alarm:

