from pymongo import MongoClient

from connection import Connection

class Database():
    def __init__(self,uri):
        
        self.port = 27017
        self._client = MongoClient(uri)

    def get_db_connection(self,coll_name,db_name='DB'):
        #creates a mongodb object
        coll_obj = self._client[db_name][coll_name]
        db_object = self._client[db_name]
        return db_object,coll_obj


    def find_all(self,coll, db_name="DB"):
        column = self._client[db_name][coll]
        fetch_all = column.find()
        return fetch_all

if __name__ == '__main__':
    conn = Connection()
    _mongo_uri = conn.create_uri()
    db = Database(_mongo_uri)
