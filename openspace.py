#!/usr/bin/python
import urllib
import urllib2
url = 'http://spaceapi.osaa.dk/sensor/set'

values = { 'key' : 'KEY' }
values["sensors"] = '{"state":{"open":true}}'

response = urllib2.urlopen(url,urllib.urlencode(values))
html = response.read()
print html
