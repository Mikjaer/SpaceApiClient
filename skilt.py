#!/usr/bin/python
import socket as soc

class Skilt:
    def __init__( self ):
	self.init();

    def init (self):
	try:
		self._address = "172.30.115" 
		self._port = 5570
		self._sock = soc.socket( soc.AF_INET, soc.SOCK_DGRAM )
		#This sets the sign to use the serial protocol so that we can do stuff
		self._sock.sendto( '\x00\x00\x00\x00\x01\x02\x03\x04\x01\x02\x03\x04\x00\x00\x00\x2B\x06', ( self._address, self._port ) )
	except:
		print "Init failed, retrying"

    def setRGB( self, red, green, blue ):
	try:
		sendstring = "\x00\x00\x00\x00\x01\x02\x03\x04\x01\x02\x03\x04\x00\x00\x00\x2A%c%c%c"%(red, green, blue )
		self._sock.sendto( sendstring, ( self._address, self._port ) )
	except:
		print "SetRGB failed, retrying"

if __name__ == '__main__':
    import sys
    s = Skilt()
#    if sys.argv[ 1 ] == "open":
#	s.setRGB( 0, 255, 0 )
 #   else:
#	s.setRGB( 255, 0, 0 )
    
