from http.server import HTTPServer, SimpleHTTPRequestHandler
try :
    HOST = "0.0.0.0"
    PORT = 8080

    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()

except KeyboardInterrupt :
    print("Interrupted by the user")