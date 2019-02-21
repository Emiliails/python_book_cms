'''
LYUtils.py
'''
class G:
    debug = True

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

 
import hashlib
def get_dic_md5(dic):
    allItems = str(dic)
    m2 = hashlib.md5(allItems.encode(encoding='UTF-8')).hexdigest()
    return m2

def is_same_dic(dict1, dict2):
    '''
    判断两个字典的值是否相同
    Keyword arguments:
    dict1 -- 字典1
    dict2 -- 字典2
    Returns: bool
    '''
    if len(dict1.items()) != len(dict2.items()):
        return False
    
    length = len(dict1.items())
    for k, v in dict1.items():
        if k in dict2.keys():
            if dict2[k] != v: 
                return False
        else:
            return False

    return True


"""
Database connect
"""
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

    def get_category(self):
        '''
        获取图书种类(category)的数据
        '''
        cCategory = self.mydb['category']
        categories = cCategory.find()
        return categories

    def insert_book_detail(self, bookInfo):
        cBook = self.mydb['books']
        cBook.insert_one(bookInfo)
        pass

    def delete_book(self, bookInfo):
        cBook = self.mydb['books']
        # update 
        myQuery = {'_id':bookInfo['_id']}
        cBook.delete_one(myQuery)
        pass

    def search(self, bookInfo):
        cBook = self.mydb['books']
        books = cBook.find(bookInfo)
        return books

    def update_book_detail(self, bookInfo): 
        cBook = self.mydb['books']
        # update 
        myQuery = {'_id':bookInfo['_id']}
        newVal = {'$set':{'name':bookInfo['name'],
                    'ISBN':bookInfo['ISBN'],
                    'jzc':bookInfo['jzc'],
                    'author':bookInfo['author'],
                    'notes':bookInfo['notes'],
                    'press':bookInfo['press'],
                    'price':bookInfo['price']}}

        cBook.update_one(myQuery, newVal)

    





