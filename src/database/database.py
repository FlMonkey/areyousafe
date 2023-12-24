from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib
import datetime

passwordhash = hashlib.sha256()

client = MongoClient(
    'ADDMONGODBCLIENT')

database = client['areyousafe']
users = database['users']
family = database['family']
messages = database['messages']


class Database:
    def __init__(self):
        self.users = users
        self.family = family
        self.messages = messages

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

    def create_family(self, familyManager, familyName, familycreater):
        familyManager = self.get_user(familyManager)['username']
        family.insert_one({'familyManager': familyManager,
                          'members': [familycreater], 'familyName': familyName})
        return True

    def join_family(self, familyID, username):
        try:
            if family.find_one({'_id': ObjectId(familyID)}):
                if username in family.find_one({'_id': ObjectId(familyID)})['members']:
                    return False
                else:
                    family.update_one({'_id': ObjectId(familyID)}, {
                                      '$push': {'members': username}})
                return True
            else:
                return False
        except:
            return False

    def get_families_for_user(self, user):
        familyList = []
        for familymember in family.find({'members': user}):
            familyList.append(familymember)
        return familyList

    def update_status(self, username, status):
        users.update_one({'username': username}, {'$set': {'status': status}})

    def get_family_members_info(self, familyID):
        familyMembers = []
        for member in family.find_one({'_id': ObjectId(familyID)})['members']:
            username = users.find_one({'username': member})['username']
            status = users.find_one({'username': member})['status']
            familyMembers.append({'username': username, 'status': status})
        return familyMembers

    def getFamilyList(self, user):
        familyList = []
        for familymember in family.find({'members': user}):
            familyList.append(familymember)
        return familyList

    def getFamilyIDbyOwner(self, user):
        familyID = family.find_one({'familyManager': user})['_id']
        return familyID

    def getFamilyMembers(self, familyID):
        for familymember in family.find({'_id': ObjectId(familyID)}):
            familyMembers = familymember['members']
        return familyMembers
