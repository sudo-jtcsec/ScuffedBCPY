import SocketServer, sys
from BaseHTTPServer import BaseHTTPRequestHandler

pathToFile = sys.argv[1]

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        pingback_file = open(pathToFile,"a")
        pingback_file.write(self.path)
        self.send_response(200)
        pingback_file.close()

httpd = SocketServer.TCPServer(("", 6996), MyHandler)
httpd.serve_forever()
