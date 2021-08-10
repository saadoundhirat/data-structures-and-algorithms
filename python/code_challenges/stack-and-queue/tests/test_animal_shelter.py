# ########################
# #test code challenge 12#
# ########################
import pytest
from stack_and_queue.animal_shelter import *

def test_add_animal():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    assert shelter.front.name == 'dog'
    
def test_dequeue_animal():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    # shelter.dequeue("dog")
    assert shelter.dequeue('dog') == 'dog'

def test_dequeue_animal_pref():
    shelter = AnimalShelter()
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    # shelter.dequeue("dog")
    assert shelter.dequeue("cat") == 'cat'
    assert shelter.dequeue("cat") == 'Your preference not found in the Animal shelter'
    assert shelter.dequeue("snake") == 'Your preference not found in the Animal shelter'