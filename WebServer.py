
from socket import *
from sys import *

port = 8080 # default web port
soc = socket(AF_INET, SOCK_STREAM)

soc.bind(('', port))
soc.listen(1)

while 1:
	clientSoc, addr = soc.accept()
	msg = clientSoc.recv(1024)
	#msg.decode()
	file = msg.split()[1]
	f = file[1:]
	
	try:
		fp = open(f,'rb')
	except:
		ok_msg = """
		HTTP/1.1 404 Not Found\n
		"""
		ok_msg = ok_msg.encode()
		clientSoc.send(ok_msg)
		clientSoc.close()
		exit()
	 
	content = fp.read()
	fp.close()

	ok_msg = """
	HTTP/1.1 200 OK\n
	Content-Type: text/html\n
	"""
	ok_msg = ok_msg.encode()
	
	clientSoc.send(ok_msg)
	clientSoc.send(content)
	clientSoc.close()

