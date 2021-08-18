############################
#####code challenge 19 #####
############################
from trees import *

def sum_odd_numbers(bst):
    """function that return the sum of odd numbers inside binary search tree"""
    output = 0
    if bst.root is None:
        return output
    
    def sum_odd_numbers_rec(root):
        nonlocal output 
        if root.value % 2 ==1:
            output += root.value
        if root.left is not None:
            sum_odd_numbers_rec(root.left)
        if root.right is not None:
            sum_odd_numbers_rec(root.right)
    
    sum_odd_numbers_rec(bst.root)
    return output


def sum_even_numbers(bst):
    """function that return the sum of even numbers inside binary search tree"""
    output = 0
    if bst.root is None:
        return output
    def sum_even_numbers_rec(root):
        nonlocal output 
        if root.value % 2 ==0:
            output += root.value
        if root.left is not None:
            sum_even_numbers_rec(root.left)
        if root.right is not None:
            sum_even_numbers_rec(root.right)
    
    sum_even_numbers_rec(bst.root)
    return output

if __name__ == "__main__":
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

    print("The some of odd numbers: ",sum_odd_numbers(bst))
    print("The some of even numbers: ",sum_even_numbers(bst))

