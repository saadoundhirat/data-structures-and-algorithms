import pytest
from hash_tables.hashtable import HashTable



# test hash table methods

def test_hash_function():
    """test the hashing function"""
    table = HashTable()
    assert table.get_hash("hello") == 532 

def test_add_item():
    """test add item to the hash table"""
    table = HashTable()
    table.addItem("hello" , 15)
    assert len(table.arr[table.get_hash("hello")]) == 1

def test_get_item():
    """test get the value from the hash table"""
    table = HashTable()
    table.addItem("hello" , 15)
    assert table.getItem("hello") == 15

def test_contains_item():
    """test check if key is inside the hash table"""
    table = HashTable()
    table.addItem("hello" , 15)
    assert table.containsItem("hello")

def test_delete_item():
    """test delete item from the hash table"""
    table = HashTable()
    table.addItem("hello" , 15)
    table.deleteItem("hello")
    assert len(table.arr[table.get_hash("hello")]) == 0
