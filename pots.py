from scapy.all import *
from time import sleep
import requests
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def send_message1():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif",
    "text": "Coffee Started",
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

def send_message2():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif",
    "text": ":coffee: Fresh Pots :coffee:",
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

def send_message3():
  data = {
    "token": "<YOUR API TOKEN>",
    "channel" : "<YOUR CHANNEL ID>",
    "icon_url" : "http://i.imgur.com/4tPGRDP.gif",
    "text": ":alarm: WARNING! Coffee Pot Powering Off!! :alarm:",
    "username": "Coffee Bot"
  }
  requests.post(SLACK_API_URL, data)

send_message1()
sleep(1020)
send_message2()
sleep(6180)
send_message3()

