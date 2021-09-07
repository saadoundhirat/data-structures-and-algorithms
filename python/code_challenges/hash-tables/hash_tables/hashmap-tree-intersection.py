## solving code code challenge 32 here 

class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class binary_tree():
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        pre_order_output = []
        if self.root == None:
            return pre_order_output

        def walk(root):
            pre_order_output.append(root.value)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return pre_order_output

def tree_intersection(tree_one,tree_two):
      output = []
      if tree_one.root == None or tree_two.root == None:
        return None
      def walk(root_one,root_two):
        if root_one.value == root_two.value:
          output.append(root_one.value)
        if root_one.left and root_two.left:
          walk(root_one.left ,root_two.left)
        if root_one.right and root_two.right :
          walk(root_one.right ,root_two.right)
      walk(tree_one.root,tree_two.root)
      return output

# from hashmap-tree-intersection.hashmap-tree-intersection import binary_tree, pre_order, tree_intersection
# def test_tree_intersection():

if __name__ == "__main__":
    tree_one = Node(150)
    tree_one.left = Node(100)
    tree_one.left.left = Node(75)
    tree_one.left.right = Node(160)
    tree_one.left.right.left = Node(125)
    tree_one.left.right.right = Node(175)
    tree_one.right = Node(250)
    tree_one.right.left = Node(200)
    tree_one.right.right = Node(350)
    tree_one.right.right.left = Node(300)
    tree_one.right.right.right = Node(500)
    binary_tree_one = binary_tree(tree_one)
    tree_two = Node(42)
    tree_two.left = Node(100)
    tree_two.left.left = Node(15)
    tree_two.left.right = Node(160)
    tree_two.left.right.left = Node(125)
    tree_two.left.right.right = Node(175)
    tree_two.right = Node(600)
    tree_two.right.left = Node(200)
    tree_two.right.right = Node(350)
    tree_two.right.right.left = Node(4)
    tree_two.right.right.right = Node(500)
    binary_tree_two = binary_tree(tree_two)
    assert tree_intersection(binary_tree_one,binary_tree_two) == [100, 160, 125, 175, 200, 350, 500]