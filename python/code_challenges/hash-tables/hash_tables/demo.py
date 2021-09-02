# implement hash tables 
# we store data inside the hash map as Key : value pairs

price = {
    'march 6': 301,
    'march 7': 430,
}

class HashTable:
    def __init__(self):
        """initialization hash table"""
        self.max = 10 #length of list
        self.arr = [None for i in range(self.max)] # or None*self.size
    
    def get_hash(self, key):
        """function to return the hash value using ASCII code"""
        h = 0
        for char in key:
            h += ord(char)
        hash_index= h % self.max 
        return hash_index
    # we use python operator to represent the method as object["key"] => __setitem__
    def add(self ,key ,value):
        """Function the store value in the key index of list"""
        h = self.get_hash(key)
        self.arr[h] = value

    # we use python operator to represent the method as object["key"] => __getitem__
    def get_item(self, key):
        """function that return the value stored in the key index"""
        h = self.get_hash(key)
        return self.arr[h]

    def find(self, key):
        pass

    def contains(self, key):
        pass
    
    def delete(self):
        pass
    


if __name__ == "__main__":
    table = HashTable()
    print (table.get_hash("march 6"))
    table.add("march 6" , 130)
    print(table.arr)
    print(table.get_item("march 6"))