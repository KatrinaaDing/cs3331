from socket import *
import sys

if len(sys.argv) == 1: 
	print("PORT NUMBER!!!!")
	exit()

port = int(sys.argv[1])
soc = socket(AF_INET, SOCK_STREAM)

soc.bind(('', port))
soc.listen(1)

while 1:
	clientSoc, addr = soc.accept()
	msg = clientSoc.recv(1024)
	
	print("\nmsg:\n" + str(msg) + "\n\n-------------------")

	# resend if header lost
	if msg == b'': continue

	# extract the file name
	file = msg.split()[1]
	f = file[1:]
	print("\nf:\n" + str(f) + "\n\n-------------------")
	
	try:
		fp = open(f, 'rb')

	# if open() failed (file not exist), 404 is sent
	except:
		fail_msg = """
		HTTP/1.1 404 Not Found


		File Not Found
		"""
		print("\nfail_msg:\n" + str(fail_msg) + "\n\n-------------------")
		fail_msg = fail_msg.encode()
		clientSoc.send(fail_msg)
		clientSoc.close()

		finish = input("finish? (y/n)")
		if finish == 'y': break

		continue
	
	# if successfully opened the file, send 200 and identify file type
	if  b'html' in f:
		ok_msg = """
		HTTP/1.1 200 OK 
		Content-Type: text/html


		"""

	elif b'png' in f:
		ok_msg = """
		HTTP/1.1 200 OK
		Content-Type: image/png


		"""
	print("\nok_msg:\n" + ok_msg + "\n\n-------------------")
	ok_msg = ok_msg.encode()

	content = fp.read()
	print("\ncontent:\n" + str(content) + "\n\n-------------------")
	fp.close()
	print("========file end==sending data========\n")

	# ok_msg += content
	clientSoc.send(ok_msg)
	clientSoc.send(content)
	# print(ok_msg)
	clientSoc.close()

	finish = input("finish? (y/n)")
	if finish == 'y': break
