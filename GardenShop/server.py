import http.server
import socketserver
import json
import pymongo

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print(self.requestline)
        if self.path == "/":
            self.send_header("Content-type", "text/html")
            f = open("index.html", "rb")
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif self.path.endswith("auth"): # The same as POST to create user
            print(self.client_address)
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
            user = json.loads(body.decode('utf-8'))
            col = db["Users"]
            query = {"email": user["e_mail"], "pass": user["password"]}
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if col.count_documents(query) == 1: # Exists in database
                self.wfile.write("http://localhost:8080/user_page.html".encode("utf-8"))
            else:
                col.insert_one(query)
                self.wfile.write("http://localhost:8080/negate.html".encode("utf-8"))
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
            f = open(path, "rb") # We need to read in bytes, to send bytes
            self.wfile.write(f.read())
            f.close()
    def do_POST(self):
        global db
        if self.path.endswith("auth"): # The same as POST to create user
            print(self.client_address)
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
            user = json.loads(body.decode('utf-8'))
            col = db["Users"]
            query = {"email": user["e_mail"], "pass": user["password"]}
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if col.count_documents(query) == 1: # Exists in database
                self.wfile.write("http://localhost:8080/user_page.html".encode("utf-8"))
            else:
                self.wfile.write("http://localhost:8080/negate.html".encode("utf-8"))
        else:
            print(self.requestline)
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            print(post_body)
            new_user = json.loads(post_body.decode('utf-8')) # As we receive bytes we need to decode
            print(new_user)
            col = db["Users"]
            query = {"email": new_user["e_mail"], "pass": new_user["password"]}
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if col.count_documents(query) == 1:
                self.wfile.write("No".encode("utf-8"))
            else:
                query = {"email": new_user["e_mail"], "pass": new_user["password"], "logged": "no"}
                col.insert_one(query)
                self.wfile.write("Yes".encode("utf-8"))

def main():
    global db
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect do database
    db = client["GardenShopDB"]
    PORT = 8080
    Handler = HandleRequests
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()