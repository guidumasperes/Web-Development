import http.server
import socketserver
import json
import pymongo

def customize_user_created(e_mail, password):
    fin = open("user_created/user_created.html", "rt")
    fout = open("user_created/user_" + e_mail + "_created.html", "wt")
    for line in fin:
        fout.write(line.replace("?", e_mail))
    fin.close()
    fout.close()
    fin = open("user_created/user_" + e_mail + "_created.html", "rt")
    data = fin.read()
    data = data.replace("#", password)
    fin.close()
    fin = open("user_created/user_" + e_mail + "_created.html", "wt")
    fin.write(data)
    fin.close()

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path == "/":
            self.send_header("Content-type", "text/html")
            f = open("index.html", "rb")
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        else:
            if self.path.endswith("?"): # I don't know why i'm getting extra GET requests with "?" at the end
                pass
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
        if self.path.endswith("cart.html"):
            content_len = int(self.headers.get('Content-Length')) # Make function to read content
            body = self.rfile.read(content_len)
            items = json.loads(body.decode('utf-8'))
            print(items)
            self.send_response(200) # Make function to set header later
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("http://localhost:8080/cart.html".encode("utf-8"))
        elif self.path.endswith("my_user_page.html"): # The same as POST to create user
            print(self.client_address)
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
            user = json.loads(body.decode('utf-8'))
            col = db["Users"]
            query = {"email": user["e_mail"], "pass": user["password"]}
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if col.count_documents(query) == 1: # Exists in database
                newvalues = {"$set": {"logged": "yes"}}
                col.update_one(query, newvalues)
                self.wfile.write("http://localhost:8080/user_page.html".encode("utf-8"))
            else:
                self.wfile.write("http://localhost:8080/negate.html".encode("utf-8"))
        else:
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
                self.wfile.write("http://localhost:8080/user_not_created.html".encode("utf-8"))
            else:
                query = {"email": new_user["e_mail"], "pass": new_user["password"], "logged": "no"}
                col.insert_one(query)
                customize_user_created(new_user["e_mail"], new_user["password"])
                self.wfile.write(bytes("http://localhost:8080/user_created/user_" + new_user["e_mail"] + "_created.html", "utf-8"))

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