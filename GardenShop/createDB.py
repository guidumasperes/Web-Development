import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["GardenShopDB"]

collectionOne = db["Users"] # Every user has a email, password and login stuts
collectionTwo = db["Products"]
collectionThree = db["Carts"] # Every user has a cart

dic = {"email": "ricardo@hotmail.com", "pass": "R13", "logged": "no", "i_address": "none"}

collectionOne.insert_one(dic)