###########################
#####code challenge 15#####
###########################

# tree implementation 
class Node:
    def __init__(self , value=None):
        self.value = value
        self.next = None
    # def __str__(self):
    #     return str(self.value)
    
class Stack:
    def __init__(self , node=None):
        self.top = node
    
    def __str__(self):
        if self.top == None:
            return 'Stack is empty'
        else:
            output = ''
            while self.top != None:
                output += str(self.top) + '\n'
                self.top = self.top.next
            return output

    def push(self, value):
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top == None:
            return None
        else:
            output = self.top
            self.top = self.top.next
            return output
    
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.value
    
    def isEmpty(self):
        return self.top == None

class Queue:
    def __init__(self , node=None):
        self.front= node
        self.rear = node
    
    def __str__(self):
        if self.front == None:
            return 'Queue is empty'
        else:
            output = ''
            while self.front != None:
                output += str(self.front) + '\n'
                self.front = self.front.next
            return output


    def enqueue(self, value):
        node = Node(value)
        if self.rear == None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front == None:
            return None
        else:
            output = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            return output

    def isEmpty(self):
        """return true if the queue is empty and false if it is not empty"""
        return self.front == None
    
    def peek(self):
        if self.front == None:
            return None
        else:
            return self.front.value
    
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

    def pre_order(self):
        """"traverse tree recursively"""
        output = []
        def traverse(root):
            # print the root node
            # print(root.value)
            output.append(root.value)
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
        traverse(self.root)
        return output


    def in_order(self):
        """"traverse tree recursively"""
        output = []
        def traverse(root):
            # print the root node
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)

            # print(root.value)
            output.append(root.value)

            if root.right is not None:
                traverse(root.right)
        traverse(self.root)
        return output

    def post_order(self):
        """"traverse tree recursively"""
        output = []
        def traverse(root):
            # print the root node
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)

            if root.right is not None:
                traverse(root.right)

            # print(root.value)
            output.append(root.value)

        traverse(self.root)
        return output

    def pre_order_iterative(self):
        """traverse tree iteratively"""
        stack = Stack()
        stack.push(self.root)
        while not stack.isEmpty():
            node = stack.pop()
            print(node.value)
            
            if node.value.right:
                stack.push(node.value.right)
            if node.value.left:
                stack.push(node.value.left)  
                
    def tree_max(self):
        """find max value in tree"""
        if self.root is None:
            return None
        max = self.root.value
        def find_max(root):
            nonlocal max
            if root.value > max:
                max = root.value
            if root.left is not None:
                find_max(root.left)
            if root.right is not None:
                find_max(root.right)
        find_max(self.root)
        return max

    # def breadth_first(self):
    #     """traverse tree using breadth first"""
    #     output = []
    #     count = 0
    #     if self.root is None:
    #         return output
    #     queue = []
    #     queue.append(self.root)
    #     while len(queue) > 0:
    #         count += 1
    #         node = queue.pop(0)
    #         output.append(node.value)
    #         if node.left is not None:
    #             print("llllllllll")
    #             queue.append(node.left)
    #         if node.right is not None:
    #             queue.append(node.right)
    #     print("count", count)
    #     return output

    def breadth_first(self):
        """traverse tree using breadth first"""
        output = []
        count = 0
        if self.root is None:
            return output
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            count += 1
            node = queue.dequeue().value
            output.append(node.value)
            if node.left is not None:
                print("llllllllll")
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        print("count", count)
        return output
        
class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        """Adds a value to the BST"""
        if self.root is None:
            self.root = TNode(value)
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = TNode(value)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = TNode(value)
                        return
                    current = current.right


    def contains(self, value):
        """Returns True if value is in the BST, False otherwise"""
        current = self.root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False


if __name__ == "__main__":
    # tree = BinaryTree()
    # tree.root = TNode("a")
    # tree.root.left = TNode("b")
    # tree.root.right = TNode("c")
    # tree.root.right.left = TNode("d")
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    # tree.pre_order_iterative()

    # tree = BinarySearchTree()
    # tree.add(20)
    # tree.add(15)
    # tree.add(10)
    # tree.add(16)
    # tree.add(30)
    # tree.add(25)
    # tree.add(35)
    # print("pre_order")
    # tree.pre_order()
    # print("in_order")
    # tree.in_order()
    # print("post_order")
    # tree.post_order()
    # print("If tree contains value= 20 =>" ,tree.contains(20))
    # print("If tree contains value= 45 =>",tree.contains(45))

#######lab 16 max value in binary tree#########
    # tree = BinaryTree()
    # tree.root = TNode(10)
    # tree.root.left = TNode(15)
    # tree.root.right = TNode(20)
    # tree.root.left.left = TNode(8)
    # tree.root.left.right = TNode(9)
    # tree.root.right.left = TNode(17)
    # tree.root.right.right = TNode(25)
    # print("max value in tree is:",tree.tree_max())

#######lab 17 breath first binary tree#########
    tree = BinaryTree()
    tree.root = TNode("a")
    tree.root.left = TNode("b")
    tree.root.right = TNode("c")
    tree.root.left.left = TNode("d")
    tree.root.left.right = TNode("e")
    tree.root.right.left = TNode("f")
    tree.root.right.right = TNode("g")
    print(tree.breadth_first())
