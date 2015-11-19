#!/usr/bin/python
import urllib2
import json
from pprint import pprint


def spaceIsOpen():
	response = urllib2.urlopen('http://spaceapi.osaa.dk/status/json');
	data = json.load(response) 

	return data['state']['open']


if spaceIsOpen():
	print "Spacet er aabnet"
else:
	print "NO!"

