from trees import __version__


def test_version():
    assert __version__ == '0.1.0'
    from trees.trees import Tree,BinaryTree


# test cases for binary tree 

# Can successfully instantiate an empty tree
def test_binary_tree():
    bt = BinaryTree()
    assert bt.root is None

# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal