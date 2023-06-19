# from urllib.parse import quote_plus


import urllib


class Connection(object):
    def __init__(self,host='localhost',port=27017):
        self.host = host
        self.port = port
    
    def create_uri(self,user,pwd):
        mongo_uri = ('mongodb+srv://%s:%s@cluster0.p35dfg4.mongodb.net/' %(user,pwd))
        return mongo_uri
    
    def create_mongo_uri(self):
        uname = 'root'
        pwd = 'root'

        _username = urllib.parse.quote(uname)
        _password = urllib.parse.quote(pwd)

        _mongo_uri = str(self.create_uri(_username,_password))
        return _mongo_uri

    
