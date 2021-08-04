import pytest
from linked_list.linked_list import LinkedList ,Node

# Write tests to prove the following functionality:

# 1-Can successfully instantiate an empty linked list
# 2-Can properly insert into the linked list
# 3-The head property will properly point to the first node in the linked list
# 4-Can properly insert multiple nodes into the linked list
# 5-Will return true when finding a value within the linked list that exists
# 6-Will return false when searching for a value in the linked list that does not exist
# 7-Can properly return a collection of all the values that exist in the linked list

########Solution#########

## 1-Can successfully instantiate an empty linked list
def test_instantiate_linked_list():
    object = LinkedList()
    assert object.head == None
    
## 2-Can properly insert into the linked list
def test_insert_into_linked_list():
    object = LinkedList()
    object.insert(1)
    assert object.head.value == 1

# 3-The head property will properly point to the first node in the linked list   
def test_head_point_to_the_first_node():
    # we insert node and if the head point to it then its working 
    object = LinkedList()
    object.insert(28)
    assert object.head.value == 28

# 4-Can properly insert multiple nodes into the linked list 
def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    assert ll.include(5)
    assert ll.include(4)
    assert ll.include(3)

# 5-Will return true when finding a value within the linked list that exists
def finding_value():
    object = LinkedList()
    object.insert(5)
    object.insert(25)
    object.insert(125) 
    assert object.include(125)

# 6-Will return false when searching for a value in the linked list that does not exist
def test_node_not_included():
    object = LinkedList()

# 7-Can properly return a collection of all the values that exist in the linked list
def test_return_collection():
    object=LinkedList()
    object.insert('24')
    object.insert('04')
    object.insert('1993')

    assert str(object) == '1993=>04=>24=>NULL'


# 8- test the append value function in the linked list
def test_append_value():
    object = LinkedList()
    object.append(6)
    assert object.head.value == 6    

#9- Can successfully add multiple nodes to the end of a linked list
def test_append_multi_value():
    object = LinkedList()
    object.append(6)
    object.append(7)
    object.append(8)
    assert str(object) == '6=>7=>8=>NULL'       

#10- Can successfully insert a node before a node located i the middle of a linked list
def test_insert_into_the_mid():
    llobj=LinkedList()
    llobj.append(24)
    llobj.append(1993)
    llobj.insert_before(1993,4)
    assert str(llobj) == '24=>4=>1993=>NULL'


#11- Can successfully insert a node before the first node of a linked list
def test_insert_befor_first_node():
    llobj=LinkedList()
    llobj.append(24)
    llobj.insert_before(24,4)
    assert str(llobj) == '4=>24=>NULL'

#12- Can successfully insert after a node in the middle of the linked list
def test_insert_after_node_in_middle():
    object = LinkedList()
    object.append(6)
    object.append(7)
    object.append(9)
    object.insert_after(7,8)
    assert str(object) == '6=>7=>8=>9=>NULL'       


#13- Can successfully insert a node after the last node of the linked list    
def test_insert_after_last_node():
    object = LinkedList()
    object.append(6)
    object.append(7)
    object.append(8)
    object.insert_after(8,9)
    assert str(object) == '6=>7=>8=>9=>NULL'  