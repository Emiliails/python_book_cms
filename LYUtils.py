'''
LYUtils.py
'''

'''
快速排序
'''
# enum.Enum 枚举类型
from collections import namedtuple
from enum import Enum

class Sort(Enum):
    ASC  = 1    # 升序
    DESC = 2    # 降序

# 快速排序
def swap(L, a, b):
    tmp = L[a]
    L[a]= L[b]
    L[b] = tmp

def qSrot(L, key, low, high):
    
    if low >= high:
        return
    
    tmp = L[low];
    left = low
    right = high
    
    
    while left < right:
        while right > left and L[right][key] >= tmp[key]:
            right -= 1
        while left < right and L[left][key] <= tmp[key]:
            left += 1

        if left < right:
            swap(L, left, right)
    
         
    if low != left:
        swap(L, left, low)
            
    qSrot(L, key, low, left-1)
    qSrot(L, key, left+1, high)
    
    
        
def quick_sort(L, key, sort=Sort.ASC):
    lenList = len(L) - 1
    qSrot(L, key ,0 ,lenList)
    
    if sort == Sort.DESC:
        L.reverse()


'''
Database connect
'''
import  pymongo

# 单例模式
# 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

# 装饰器版本
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
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
        cBook = self.mydb['books']
        books = cBook.find(bookInfo)
        #for book in books:
        #    print(str(book))
        return books
