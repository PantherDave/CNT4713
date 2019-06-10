from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if self.path.endswith(".mp4"):
                mimetype = 'video/mp4'
                sendReply = True
            if self.path.endswith(".mov"):
                mimetype = 'video/quicktime'
                sendReply = True
            if self.path.endswith(".wmv"):
                mimetype = 'video/x-ms-wmv'
                sendReply = True
            if self.path.endswith(".avi"):
                mimetype = 'video/x-msvideo'
                sendReply = True
            if self.path.endswith(".mp3"):
                mimetype = 'audio/mpeg'
                sendReply = True 
            if self.path.endswith(".wav"):
                mimetype = 'audio/vnd.wav'
                sendReply = True
            if self.path.endswith(".mid"):
                mimetype = 'audio/mid'
                sendReply = True

            
            if sendReply == True:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File No Found: %s' % self.path)
try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver or port', PORT_NUMBER

    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()


            
