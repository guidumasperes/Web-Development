import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["GardenShopDB"]

collectionOne = db["Users"]
collectionTwo = db["Products"]

dic = {"email": "Ricardo@hotmail.com", "pass": "R13"}

collectionOne.insert_one(dic)