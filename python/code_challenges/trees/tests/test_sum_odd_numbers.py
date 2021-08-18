from trees.sum_odd_numbers import *


def test_empty_tree():
    """Test empty tree."""
    bst = BinarySearchTree()
    assert bst.root == None

def test_sum_odd_numbers():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(10)
    bst.add(1)
    bst.add(6)
    bst.add(4)
    bst.add(7)
    bst.add(10)
    bst.add(14)
    bst.add(13)
    assert sum_odd_numbers(bst) == 24

def test_sum_even_numbers():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(10)
    bst.add(1)
    bst.add(6)
    bst.add(4)
    bst.add(7)
    bst.add(10)
    bst.add(14)
    bst.add(13)
    assert sum_even_numbers(bst) == 52