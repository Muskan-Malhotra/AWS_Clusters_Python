from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

myclient = MongoClient('mongodb+srv://admin:<password>@cluster0.z2k93et.mongodb.net/')
print(myclient.list_database_names())

mydb = myclient['Demo_Deployment']
collection = mydb["user_data"]


mylist = [
    {'datetime': datetime.now(),'username':'muskan2401','password':'pass@1234','api_hit':0},
    {'datetime': datetime.now(),'username':'siddhi100','password':'Pass#1234','api_hit':0}
]

data_insert = collection.insert_many(mylist)
dblist = myclient.list_database_names()
print(dblist)