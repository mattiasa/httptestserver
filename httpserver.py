from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os

def get_response():
    content = "<dl>"
    for key, value in os.environ.items():
        content += f"<dt>{key}</dt><dd>{value}</dd>"

    content += "</dl>"

    return bytes(content, 'utf-8')


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(get_response())


def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

    
if __name__ == '__main__':
    run()
