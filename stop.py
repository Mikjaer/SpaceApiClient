#!/usr/bin/python -W ignore

from time import sleep
import thread
import RPi.GPIO as GPIO
import urllib
import urllib2
import json
import subprocess
import skilt

from pprint import pprint


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(2, True)



s = skilt.Skilt()

GPIO.output(2, False)		
GPIO.output(3, False)		
s.setRGB( 0, 0, 255 )



