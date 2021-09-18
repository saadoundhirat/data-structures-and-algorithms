import pytest
from hash_tables.hashtable import HashTable
from hash_tables.hashmap_tree_intersection import *

def test_hashmap_tree_intersection():
    tree1= BinaryTree()
    tree1.root = TNode(150)
    tree1.root.left = TNode(100)
    tree1.root.right = TNode(250)
    tree1.root.left.left = TNode(75)
    tree1.root.left.right = TNode(160)
    tree1.root.left.right.left = TNode(125)
    tree1.root.left.right.right = TNode(175)
    tree1.root.right.left = TNode(200)
    tree1.root.right.right = TNode(350)
    tree1.root.right.right.left = TNode(300)
    tree1.root.right.right.right = TNode(500)
    

    tree2= BinaryTree()
    tree2.root = TNode(42)
    tree2.root.left = TNode(100)
    tree2.root.right = TNode(600)
    tree2.root.left.left = TNode(15)
    tree2.root.left.right = TNode(160)
    tree2.root.left.right.left = TNode(125)
    tree2.root.left.right.right = TNode(175)
    tree2.root.right.left = TNode(200)
    tree2.root.right.right = TNode(350)
    tree2.root.right.right.left = TNode(4)
    tree2.root.right.right.right = TNode(500)

    hashtable = HashTable()
    tree = BinaryTree()
    intersectionList = tree.tree_intersection(tree1, tree2 , hashtable)
    assert intersectionList == [100, 160, 125, 175, 200, 350, 500]