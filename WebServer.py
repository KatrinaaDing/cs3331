
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

port = 8080
addr = ('localhost', port)

# Handler = http.server.SimpleHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    
    # Parse and get the request to determine the specific file
    def do_GET(self):
    	# self.send_response(200)
        if self.path == '/':
            self.path == ('/index.html')

        try:
        	file_to_open = open(self.path[1:].read())
        	self.send_response(200)

        except:
        	file_to_open = "File Not Found"
        	self.send_error(404)
        
#    def send_error(error_message_format, message=None):
#    	print("dfdfd")


# receive HTTP request from connection.

server = HTTPServer(addr,handler)

print('server started at ' + port)

server.serve_forever()

'''

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
'''