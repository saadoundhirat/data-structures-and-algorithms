########################
#######lecture 15#######
########################

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
            return output

    def isEmpty(self):
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
        def traverse(root):
            # print the root node
            print(root.value)
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
        traverse(self.root)

    def in_order(self):
        """"traverse tree recursively"""
        def traverse(root):
            # print the root node
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)

            print(root.value)

            if root.right is not None:
                traverse(root.right)
        traverse(self.root)

    def post_order(self):
        """"traverse tree recursively"""
        def traverse(root):
            # print the root node
            # traverse left & right subtree
            if root.left is not None:
                traverse(root.left)

            if root.right is not None:
                traverse(root.right)

            print(root.value)

        traverse(self.root)


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
                
    def breadth_First(self):
        """traverse tree breadth first"""
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    
    def add(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return
        current = self.root
        while current:
            if current.value > value: 
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
            if current.value < value:
                if current.left:
                   current = current.left
                else:
                    current.left = node
                    return

    def contains(self, value):
        if value == self.root:
            return True
        current = self.root
        while current:
            if current.value > value: 
                if current.right:
                   current = current.right
                else:
                    return False
            if current.value < value:
                if current.left:
                   current = current.left 
                else:
                    return False
            if current.value == value:
                return True  
        return False


if __name__ == "__main__":
    # tree = BinaryTree()
    # tree.root = TNode("a")
    # tree.root.left = TNode("b")
    # tree.root.right = TNode("c")
    # tree.root.right.left = TNode("d")
    # tree.pre_order_iterative()
    # tree.pre_order()
    # tree.in_order()
    # tree.post_order()

    tree = BinarySearchTree()
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    tree.add(18)
    tree.contains(tree.root, 20)


# class KNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.children = []