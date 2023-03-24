from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    'mongodb+srv://monkey:DI8sSfUPHVGFgsoH@areyousafe.yem7rhp.mongodb.net/?retryWrites=true&w=majority')

database = client['areyousafe']
users = database['users']
family = database['family']


class Database:
    def __init__(self):
        self.users = users
        self.family = family


    def get_user(self, username):
        return users.find_one({'username': username})
    
    def register(self, username, password, status):
        if users.find_one({'username': username}):
            return False
        else:
            users.insert_one({'username': username, 'password': password, 'status': status})
            return True
        
    def login(self, username, password):
        if users.find_one({'username': username, 'password': password}):
            return True
        else:
            return False
