
from socket import *

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
	fp = open(f)
	content = fp.read()
	content = content.encode()
	# print(content)
	fp.close()
	clientSoc.send(content)

clientSoc.close()
