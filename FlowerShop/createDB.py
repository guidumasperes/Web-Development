import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["FlowerShopDB"]

collectionOne = db["Users"]
collectionTwo = db["Products"]

dic = {"email": "Ricardo", "pass": "R13"}

collectionOne.insert_one(dic)