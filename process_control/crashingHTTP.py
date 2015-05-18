import BaseHTTPServer
import urlparse
import sys

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class MyHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		real_path = parsed_path.path
		if 'error' in real_path:
			sys.exit(1)
		else:
			address = self.client_address
			self.send_response(200)
			self.end_headers()
			self.wfile.write(address) 
                
run(BaseHTTPServer.HTTPServer, MyHTTPHandler)
