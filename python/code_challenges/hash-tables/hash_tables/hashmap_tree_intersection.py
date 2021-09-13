## solving code code challenge 32 here 
from hash_tables.hashtable import HashTable
# from hash_tables.tree import *
class TNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.table = HashTable()

    def tree_intersection(self ,tree1, tree2):
        """
        Given two binary search trees, return a list containing all the values from
        both trees that are the same.    
        >>> tree1 = create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> tree2 = create_tree([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        >>> tree_intersection(tree1, tree2)
        [2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        listtree1 = tree1.pre_order() 
        listtree2 = tree2.pre_order()
        intersection = []
        for i in listtree1:
            for j in listtree2:
                if i == j:
                    intersection.append(i)
        return intersection

    def pre_order(self):
            """"traverse tree recursively"""
            intersection = []
            def traverse(root):
                if root is None: return intersection 

                intersection.append(root.value)

                if root.left is not None:
                    traverse(root.left)

                if root.right is not None:
                    traverse(root.right)
            traverse(self.root)
            return intersection

if __name__ == "__main__":
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


    tree = BinaryTree()
    intersectionList = tree.tree_intersection(tree1, tree2)
    print(intersectionList)