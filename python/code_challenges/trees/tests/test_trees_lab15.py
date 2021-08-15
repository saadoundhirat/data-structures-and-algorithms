from trees.trees import *

#############Write tests to prove the following functionality###########

## Can successfully instantiate an empty tree
def test_empty_tree():
    """Can successfully instantiate an empty tree"""
    tree = BinaryTree()
    assert tree.root is None
    
## Can successfully instantiate a tree with a single root node
def test_tree_with_one_node():
    """Can successfully instantiate a tree with a single root node"""
    tree = BinaryTree()
    tree.root = TNode(1)
    assert tree.root.value == 1
    
## Can successfully instantiate a tree with a single root node
def test_tree_with_two_nodes():
    """Can successfully instantiate a tree with a single root node"""
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    assert tree.root.left.value == 2
    

## Can successfully add a left child and right child to a single root node
def test_add_left_and_right_child():
    """Can successfully add a left child and right child to a single root node"""
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    


## Can successfully return a collection from a preorder traversal
def test_preorder_traversal():
    """Can successfully return a collection from a preorder traversal"""
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    tree.root.right.right = TNode(7)
    assert tree.pre_order() == [1,2,4,5,3,6,7]
    


## Can successfully return a collection from an in order traversal
def test_inorder_traversal():
    """Can successfully return a collection from an in order traversal"""
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    tree.root.right.right = TNode(7)
    assert tree.in_order() == [4,2,5,1,6,3,7]

## Can successfully return a collection from a postorder traversal
def test_postorder_traversal():
    """Can successfully return a collection from a postorder traversal"""
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    tree.root.right.right = TNode(7)
    assert tree.post_order() == [4,5,2,6,7,3,1]