

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

port = 8080
addr = ('localhost', port)

# Handler = http.server.SimpleHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    
    # Parse and get the request to determine the specific file
    def do_GET(self):
    	print (self.path)

        try:
        	# f = open(self.path[1:])
        	self.rfile(self.path[1:])
        	self.send_response(200)
        except:
        	file_to_open = "File Not Found"
        	self.send_error(404)
        
#    def send_error(error_message_format, message=None):
#    	print("dfdfd")


# receive HTTP request from connection.

server = HTTPServer(addr,handler)

print('server started at ', port)

server.serve_forever()


'''

import http.server
import socketserver
# 
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
'''
'''
from socket import *

port = 80 # default web port
soc = socket(AF_INET, SOCK_STREAM)

soc.bind(('', port))
soc.listen(1)

while 1:
	clientSoc, addr = soc.accept()
	msg = clientSoc.recv(1024)
	file = msg.split()[1]
	f = open(file[1:])

	clientSoc.send(f.read())
	clientSoc.close()
'''


'''
    	# self.send_response(200)
        if self.path == '/':
            self.path = ('/index.html')
'''