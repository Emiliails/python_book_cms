'''
LYUtils.py
'''

'''
Database connect
'''
import  pymongo

class DBManager(object):

    def __init__(self):
        self.myClient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.mydb = self.myClient['test']

    def check_user(self, username, password):
        cUser = self.mydb['test']
        count = cUser.find({'name':username,'pwd':password}).count()
        if count > 0:
            print('find user!')
            return True

        print('illege user!')
        return False

    def insert(self, bookInfo):
        pass

    def delete(self, bookInfo):
        pass

    def search(self, bookInfo):
        pass
