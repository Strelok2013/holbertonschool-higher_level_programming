#!/usr/bin/python3
import http.server
import socketserver
import json

hostname = "localhost"
port = 8000

class Server(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        json_data = json.dumps({"name":"John", "age": 30, "city":"New York"})
        json_data2 = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
        if self.path == "/data":
            self.send_response(200)
            self.wfile.write(bytes(json_data, "utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.wfile.write(bytes("OK", "utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.wfile.write(bytes(json_data2, "utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))
        else:
            self.send_response(404)
            self.wfile.write(bytes("Endpoint not found", "utf-8"))
        

serv = http.server.HTTPServer((hostname, port), Server)

print("server starting")
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass

serv.server_close()
print("server closing")