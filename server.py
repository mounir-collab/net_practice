# from http.server import HTTPServer, SimpleHTTPRequestHandler
# try :
#     HOST = "0.0.0.0"
#     PORT = 8080

#     server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

#     print(f"Server running at http://{HOST}:{PORT}")
#     server.serve_forever()

# except KeyboardInterrupt :
#     print("Interrupted by the user")



import requests



url = "https://profile-v3.intra.42.fr/"

response = requests.get(url)

print("Status code:", response.status_code)
print("Headers:", response.headers)
print("Body:")
print(response.text)