import cec
from time import sleep
from os import system


def tv_on():
  system("sudo -u pulse pactl set-sink-input-mute 0 1")

def tv_off():
  system("sudo -u pulse pactl set-sink-input-mute 0 0")

def handler(a, b, c, d):
  if d == "TV (0): power status changed from 'standby' to 'on'" or d == "TV (0): power status changed from 'unknown' to 'on'" :
    tv_on()

  if d == "TV (0): power status changed from 'on' to 'standby'" or d == "TV (0): power status changed from 'unknown' to 'standby'" :
    tv_off()

cec.init()
tv_off()  # default
cec.add_callback(handler, cec.EVENT_ALL)

while True:
  sleep(1)

