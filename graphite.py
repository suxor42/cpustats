#graphite send_data

import socket

__graphite_server = "localhost"
__graphite_port = 2003
__soc = None

def connect():
	global __soc
	__soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	__soc.connect( (__graphite_server,__graphite_port) )

def close():
	global __soc
	__soc.shutdown(SHUT_RDWR)
	__soc.close()

def send_data(path,value,timstamp):
	global __soc

	#print "%s %s %s" % (path,value,timstamp)
	__soc.sendall(str.encode("%s %s %s\n" % (path,value,timstamp)) )
	#__soc.flush()
	#__soc.close()
