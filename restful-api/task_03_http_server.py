#!/usr/bin/python3
"""
This module provides an http server
"""

import http.server
import socketserver
import json

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type="text/html"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Content-Security-Policy", "default-src 'self'")
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_response()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self._set_response(content_type="application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_response(content_type="application/json")
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self._set_response(404)
            self.wfile.write("Endpoint not found".encode('utf-8'))

    def log_message(self, format, *args):
        # Suppress logging to avoid leaking information
        return


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)

    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()


if __name__ == '__main__':
    run(server_class=socketserver.TCPServer)
