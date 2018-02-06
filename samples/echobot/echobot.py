import http.server
import json

class BotHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = self.headers['content-length']
        length = int(content_length) if content_length else 0
        
        content = self.rfile.read(length)
        activity = json.loads(content)
        
        self.send_response(202)

if __name__ == '__main__':
    PORT = 3978
    httpd = http.server.HTTPServer(("", PORT), BotHandler)

    print (httpd.server_name, " listening to ", httpd.server_port)
    httpd.serve_forever()