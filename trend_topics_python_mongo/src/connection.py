from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

db = client.dio_live

trends_collection = db.trends
