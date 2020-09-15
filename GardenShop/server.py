import http.server
import socketserver
import json
import pymongo

#TO DO:
#1)Logout feature (OK)
#2)Check if user is logged before buying
#3)Customized user_page
#4)Negation page
#5)Add responsive designs
#6)Add user home address to database in "Users" to make things more realistic
#7)Remove from cart
#8)Order
#9)Add a history of orders to user_page

def customize_user_created(e_mail, password):
    fin = open("user_created/user_created_template.html", "rt")
    fout = open("user_created/user_created.html", "wt")
    for line in fin:
        fout.write(line.replace("?", e_mail))
    fin.close()
    fout.close()
    fin = open("user_created/user_created.html", "rt")
    data = fin.read()
    data = data.replace("#", password)
    fin.close()
    fin = open("user_created/user_created.html", "wt")
    fin.write(data)
    fin.close()

def customize_user_cart(items):
    print(items)
    fin = open("carts/template_cart.html", "rt")
    fout = open("carts/cart.html", "wt")
    to_write = ""
    for i in items:
        to_write = to_write + "\t\t\t<li>" + i + "</li><button>Remove</button>\n"
    print(to_write)
    for line in fin:
        fout.write(line.replace("%", to_write))
    fin.close()
    fout.close()

def assign_cart_to_user(items, user_address):
    global db
    cart_col = db["Carts"]
    query = {"items": items, "user_address": user_address}
    cart_col.insert_one(query)

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
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
        if self.path.endswith("cart.html"): # Cart feature
            print(self.client_address)
            content_len = int(self.headers.get('Content-Length')) # Make function to read content
            body = self.rfile.read(content_len)
            items = json.loads(body.decode('utf-8'))
            print(items)
            self._set_headers()
            customize_user_cart(items)
            assign_cart_to_user(items, self.client_address[0]) # The user with this IP is assigned to this cart
            self.wfile.write("http://localhost:8080/carts/cart.html".encode("utf-8"))
        elif self.path.endswith("user_page.html"): # Login feature, the same as POST to create user
            print(self.client_address)
            content_len = int(self.headers.get('Content-Length'))
            body = self.rfile.read(content_len)
            user = json.loads(body.decode('utf-8'))
            col = db["Users"]
            query = {"email": user["e_mail"], "pass": user["password"]}
            self._set_headers()
            if col.count_documents(query) == 1: # Exists in database
                newvalues = {"$set": {"logged": "yes", "i_address": self.client_address[0]}}
                col.update_one(query, newvalues)
                self.wfile.write("http://localhost:8080/user_page.html".encode("utf-8"))
            else:
                self.wfile.write("http://localhost:8080/negate.html".encode("utf-8"))
        elif self.path.endswith("logout_page.html"): # Logout
            print(self.client_address)
            col = db["Users"]
            query = {"i_address": self.client_address[0]}
            newvalues = {"$set": {"logged": "no"}}
            col.update_one(query, newvalues)
            self._set_headers()
            self.wfile.write("http://localhost:8080/logout_page.html".encode("utf-8"))
        else: # Create account feature
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            print(post_body)
            new_user = json.loads(post_body.decode('utf-8')) # As we receive bytes we need to decode
            print(new_user)
            col = db["Users"]
            query = {"email": new_user["e_mail"], "pass": new_user["password"]}
            self._set_headers()
            if col.count_documents(query) == 1:
                self.wfile.write("http://localhost:8080/user_not_created.html".encode("utf-8"))
            else:
                query = {"email": new_user["e_mail"], "pass": new_user["password"], "logged": "no", "i_address": self.client_address[0]}
                col.insert_one(query)
                customize_user_created(new_user["e_mail"], new_user["password"])
                self.wfile.write(bytes("http://localhost:8080/user_created/user_created.html", "utf-8"))

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