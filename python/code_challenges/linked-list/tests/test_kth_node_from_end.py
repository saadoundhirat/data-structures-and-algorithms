# lab 07 test folder 
from linked_list.linked_list import LinkedList ,Node

#1- Where k is greater than the length of the linked list
def test_if_k_bigger_than_numof_node():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    x=ll.getKthNodeFromEnd(20)
    assert x == "Number of K is bigger than the number of Nodes !!!"

#2- Where k and the length of the list are the same
def test_if_k_and_lengthof_node_same():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    # ll.getKthNodeFromEnd(5)
    assert str(ll.getKthNodeFromEnd(5)) == "5"



#3- Where k is not a positive integer
def test_if_k_not_positive_integer():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    x = ll.getKthNodeFromEnd(-12)
    assert x == "K is negative"

#4- Where the linked list is of a size 1
def test_ll_size_1():
    ll = LinkedList()
    ll.append(5)
    assert str(ll.getKthNodeFromEnd(0))=="5"

#5- “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    # ll.getKthNodeFromEnd(5)
    assert str(ll.getKthNodeFromEnd(3)) == "7"