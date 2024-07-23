# serve_html.py

import http.server
import socketserver
import threading

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Audio Stream</title>
</head>
<body>
    <iframe id="video" width="640" height="360" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</body>
</html>
"""

# Save the HTML template to a file
with open("index.html", "w") as file:
    file.write(HTML_TEMPLATE)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

def start_server():
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Keep the server running
try:
    while True:
        pass
except KeyboardInterrupt:
    httpd.shutdown()
