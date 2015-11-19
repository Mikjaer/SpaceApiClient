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


def spaceIsOpen():
	global error
        try:
		response = urllib2.urlopen('http://spaceapi.osaa.dk/status/json');
        	data = json.load(response)

		error = 0
        	return data['state']['open']
	except:
		error = 1
		print "SpaceIsOpen failed"
		return "unknown";

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(2, True)


error = 0
s = skilt.Skilt()

def setSpaceState( state ):
	global error
	url = 'http://spaceapi.osaa.dk/sensor/set'

	values = { 'key' : 'KEY' }
	if state == "open":
		values["sensors"] = '{"state":{"open":true}}'
	else:
		values["sensors"] = '{"state":{"open":false}}'
	
	try:
		response = urllib2.urlopen(url,urllib.urlencode(values))
		html = response.read()
		monitorSpace()
		error = 0 
	except:
		print "setSpaceState failed"
		error = 1
	
def monitorSpaceThread():
	while 1:
		monitorSpace()
		sleep(10)

def monitorSpace():
	global error
	if spaceIsOpen():
		GPIO.output(2, False)		
		GPIO.output(3, True)		
        	s.setRGB( 0, 255, 0 )

	else:
		GPIO.output(3, False)		
		GPIO.output(2, True)		
		s.setRGB( 255, 0, 0 )
	if error == 1:
		GPIO.output(3, True)
		GPIO.output(2, True)
	

try:
	thread.start_new_thread( monitorSpaceThread, ())
except:
	print "Error: unable to start thread"


while 1:
	if not GPIO.input(4):
		if spaceIsOpen():
			print "Space is open, closing";
			setSpaceState("closed")
		else:
			print "Space is closed, opening";
			setSpaceState("open")
		sleep(1)		




