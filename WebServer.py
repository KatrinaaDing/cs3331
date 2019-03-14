import http.server

PORT = 8080

# Handler = http.server.SimpleHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    
    # Parse and get the request to determine the specific file
    def do_GET(self):
        if self.path == ('/'):
            self.path == ('/index.html')



# receive HTTP request from connection.
try:
    server = HTTPServer('localhost',handler)
    
    print('server started')
    
    server.serve_forever();

except KeyboardInterrupt as e:
    print 'shutting down the serrver'
    server.close_connection()

