import pytest
from hash_tables.hashtable import HashTable
from hash_tables.hashmap_left_join import left_join


def test_left_join_empty_hashmap():
    ht1 =HashTable ()
    ht2 =HashTable ()
    assert left_join(ht1 , ht2) == []

def test_left_join_hashmap():
    ht1 = HashTable()
    ht1.addItem("fond", "enamored")
    ht1.addItem("wrath", "anger")
    ht1.addItem("diligent", "employed")
    ht1.addItem("outfit", "garb")
    ht1.addItem("guide", "usher")

    ht2 = HashTable()
    ht2.addItem("fond", "averse")
    ht2.addItem("wrath", "delight")
    ht2.addItem("diligent", "idle")
    ht2.addItem("guide", "follow")
    ht2.addItem("flow", "jam")

    assert left_join(ht1, ht2) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['flow', None, 'jam']]