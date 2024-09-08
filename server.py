from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return super().do_GET()

with HTTPServer(('', PORT), MyHandler) as server:
    print(f'Serving on port {PORT}')
    server.serve_forever()
