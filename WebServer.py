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
	print("\nListening...")
	clientSoc, addr = soc.accept()
	msg = clientSoc.recv(1024)
	
	# print("\nmsg:\n" + str(msg) + "\n\n-------------------")

	# resend if header lost
	if msg == b'': continue

	# extract the file name
	file = msg.split()[1]
	f = file[1:]
	print(f"Trying to open file {f}")
	# print("\nf:\n" + f + "\n\n-------------------")

	# only identifying .html and .png
	if b'html' not in f and b'png' not in f: continue 

	try:
		fp = open(f, 'rb')

	# if open() failed (file not exist), 404 is sent
	except:
		fail_msg = b"""
		HTTP/1.1 404 Not Found


		404 File Not Found
		"""
		# print("\nfail_msg:\n" + str(fail_msg) + "\n\n-------------------")
		clientSoc.send(fail_msg)
		print("Sorry, file not found")
		clientSoc.close()
		'''
		finish = input("\nWish to continue? (y/n)")
		if finish == 'n': break
		'''
		continue
	
	# if successfully opened the file, send 200 and identify file type
	if  b'html' in f:
		ok_msg = b"""
		HTTP/1.1 200 OK 
		Content-Type: text/html


		"""

	elif b'png' in f:
		ok_msg = b"""
		HTTP/1.1 200 OK
		Content-Type: image/png


		"""
	
	# print("\nok_msg:\n" + ok_msg + "\n\n-------------------")
	content = fp.read()
	print("Reading file...")
	#print("\ncontent:\n" + str(content) + "\n\n-------------------")
	fp.close()
	print("Sending data...")

	# ok_msg += content
	clientSoc.send(ok_msg)
	clientSoc.send(content)
	print("File is successfully sent\n")
	clientSoc.close()
	'''
	finish = input("\nWish to continue? (y/n)")
	if finish == 'n': break
	'''