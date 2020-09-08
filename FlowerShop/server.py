import http.server
import socketserver

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path == "/":
            self.send_header("Content-type", "text/html")
            f = open("index.html", "rb")  # change for index.html later
            self.end_headers()
            self.wfile.write(f.read())
        else:
            if self.path.endswith(".html"):
                self.send_header("Content-type", "text/html")
            elif self.path.endswith(".css"):
                self.send_header("Content-type", "text/css")
            elif self.path.endswith(".jpg"):
                self.send_header("Content-type", "image/jpeg")
            else:
                self.send_header("Content-type", "text/javascript")
            path = self.path[1:]
            self.end_headers()
            f = open(path, "rb")
            self.wfile.write(f.read())
        f.close()
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Received POST request with body: ".encode("utf-8") + post_body)

def main():
    PORT = 8080
    Handler = HandleRequests
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()