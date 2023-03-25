from pymongo import MongoClient
from bson.objectid import ObjectId
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
            if user['password'] == hashedPass:
                return True

    def create_family(self, familyManager, familyName):
        familyManager = self.get_user(familyManager)['username']
        family.insert_one({'familyManager': familyManager,
                          'members': [], 'familyName': familyName})
        return True

    def join_family(self, familyID, username):
        try:
            if family.find_one({'_id': ObjectId(familyID)}):
                family.update_one({'_id': ObjectId(familyID)}, {
                                  '$push': {'members': username}})
                return True
            else:
                return False
        except:
            return False

    def get_families_for_user(self, user):
        familyList = []
        families = self.family.find({'members': user['username']})
        for family in families:
            for member in family['members']:
                familyList.append(self.get_user(member))
            
        return familyList
        
