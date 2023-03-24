from pymongo import MongoClient
import hashlib

passwordhash = hashlib.sha256()

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
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if users.find_one({'username': username}):
            return False
        else:
            users.insert_one(
                {'username': username, 'password': password, 'status': status})
            return True

    def login(self, username, passwordtocheck):

        user = self.get_user(username)
        hashedPass = hashlib.sha256(
            passwordtocheck.encode('utf-8')).hexdigest()

        if users.find_one({'username': username}):
            print('user found')
            print(user['password'])
            if user['password'] == hashedPass:
                print('password correct')
                return True
