# implement hash tables 
# we store data inside the hash map as Key : value pairs
from hash_tables.linked_list import *
import re

class HashTable:
    def __init__(self ,size = 1024):
        """initialization hash table"""
        self.max = size #length of list
        self.arr = [[] for i in range(self.max)] # or [None]*self.size\ we store key value pairs in each index [('Key' , value),('Key' , value) ]

    def get_hash(self, key):
        """function to return the hash value using ASCII code"""
        h = 0
        for char in key:
            h += ord(char)
        hash_index= h % self.max 
        return hash_index

    
    def addItem(self ,key ,value):
        """Function the store key value pairs in the key index of list"""
        h = self.get_hash(key)
        found = False
        # we have to loop in the linked list to check if the key is found then update its value 
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found: # if not found store it 
            self.arr[h].append((key,value))



    def getItem(self, key):
        """function that return the value stored in the key index"""
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1] # return the value

    def containsItem(self, key):
        h = self.get_hash(key)
        found = False
        # we have to loop in the linked list to check if the key is found then update its value 
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                found = True
        return found


    def deleteItem(self , key):
        """function that set the value of key to None"""
        h = self.get_hash(key)
        for idx , element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
    
    def keys(self):
        """function that return all keys in the hash table"""
        keys = []
        for element in self.arr:
            for key in element:
                keys.append(key[0])
        return keys

def repeated_word(str):
    if str == "":
        return str

    strings = re.sub(r'[^\w\s]','',str).lower().split(' ')
    print("the string is " , strings)

    hash_table = HashTable()
    for element in strings:
        if hash_table.containsItem(element):
            return element
        else:
            hash_table.addItem(element,1)
    return 'nothing is duplicated...'


# if __name__ == "__main__":
#     # table = HashTable()
#     # table.addItem('march 18' , 0)
#     # table.addItem('march 19' , 100)
#     # table.addItem('march 20' , 200)
#     # table.addItem('march 10' , 300)
#     # table.addItem('march 6' , 400)
#     # table.addItem('march 17' , 500)

#     # for idx in table.arr:
#     #     print(idx)
    
#     # print("======================")
#     # table.addItem('march 6' , 400)    
#     # print(table.containsItem('march 6'))
#     # table.deleteItem('march 6')
#     # table.deleteItem('march 20')
#     # print(table.getItem('march 6'))

#     # for idx in table.arr:
#     #     print(idx)

#     print(repeated_word("Once upon a time, there was a brave princess who..."))
#     print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
#     print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."))