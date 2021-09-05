import pytest
from hash_tables.hashtable import HashTable, repeated_word



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


#=========================
# test repeated_word

def test_repeated_word():
    "test repeated_word"

    assert repeated_word('') == ''
    assert repeated_word("Once upon a time, there was a brave princess who...") == 'a'
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York...") == 'summer'