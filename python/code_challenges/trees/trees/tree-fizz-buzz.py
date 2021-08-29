###########################
#####code challenge 18#####
###########################
import copy

# Feature Tasks
# Write a function called fizz buzz tree
# Arguments: k-ary tree
# Return: new k-ary tree


class K_TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child): #child is a tree node 
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        """print_K-tree"""
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def fizz_buzz_tree(root):
    """fizz buzz tree"""
    # If the value is divisible by 3, replace the value with “Fizz”
    # If the value is divisible by 5, replace the value with “Buzz”
    # If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    # If the value is not divisible by 3 or 5, simply turn the number into a String.
    # Return the new k-ary tree.

    # make new GTreeNode
    # new_root = copy.deepcopy(root)

    if root is None:
        return None
    if root.data % 3 == 0 and root.data % 5 == 0:
        root.data = "fizzbuzz"
    elif root.data % 3 == 0:
        root.data = "fizz"
    elif root.data % 5 == 0:
        root.data = "buzz"
    # check if the new root has children 
    if root.children:
        for child in root.children:
            fizz_buzz_tree(child)
    return root

def print_tree(root):
        """print_K-tree"""
        print(root.data)
        if root.children:
            for child in root.children:
                child.print_tree()


if __name__ =="__main__":
    root = K_TreeNode(1)

    child1 = K_TreeNode(2)
    child1.add_child(K_TreeNode(5))
    child1.add_child(K_TreeNode(6))
    child1.add_child(K_TreeNode(7))

    child2 = K_TreeNode(3)
    child2.add_child(K_TreeNode(8))
    child2.add_child(K_TreeNode(9))
    child2.add_child(K_TreeNode(10))

    child3 = K_TreeNode(4)
    child3.add_child(K_TreeNode(11))
    child3.add_child(K_TreeNode(12))
    child3.add_child(K_TreeNode(13))
    child3.add_child(K_TreeNode(14))
    child3.add_child(K_TreeNode(15))

    # add all children to root
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    
    root.print_tree()

    print("###################################")

    general_tree = fizz_buzz_tree(root)
    print_tree(general_tree)


##############################
#####General tree traning#####
##############################
# class K_aryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
    
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)


###########################


# def build_product_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))

#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))

#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     root.print_tree()

# if __name__ == '__main__':
#     build_product_tree()


