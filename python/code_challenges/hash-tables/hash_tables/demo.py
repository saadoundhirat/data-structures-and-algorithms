# implement hash tables 
# we store data inside the hash map as Key : value pairs



## handling collisions in hash table using list 
class HashTable:
    def __init__(self):
        """initialization hash table"""
        self.max = 20 #length of list
        self.arr = [[None] for i in range(self.max)] # or [None]*self.size we only store the value here 

    def get_hash(self, key):
        """function to return the hash value using ASCII code"""
        h = 0
        for char in key:
            h += ord(char)
        hash_index= h % self.max 
        return hash_index

    def addItem(self ,key ,value):
        """Function the store value in the key index of list"""
        h = self.get_hash(key)
        self.arr[h] = value

    def getItem(self, key):
        """function that return the value stored in the key index"""
        h = self.get_hash(key)
        return self.arr[h]


    def containsItem(self, key):
        pass
    
    def deleteItem(self , key):
        """function that set the value of key to None"""
        h = self.get_hash(key)
        self.arr[h] = None
    


if __name__ == "__main__":
    table = HashTable()
    print (table.get_hash("march 6"))
    print(table.arr)
    print("===============")
    table.addItem('march 18' , 0)
    table.addItem('march 19' , 100)
    table.addItem('march 20' , 200)
    table.addItem('march 10' , 300)
    table.addItem('march 6' , 400)
    # table.addItem('march 17' , 500)
    
    print(table.getItem("march 6")) # O(1)
    print(table.arr)
   