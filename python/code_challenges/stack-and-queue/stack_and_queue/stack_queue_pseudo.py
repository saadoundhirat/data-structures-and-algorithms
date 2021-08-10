###############################################
##############code challenge 11################
###############################################


class Node:
    def __init__(self, data:None):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        # to print the stack we just call the function that prints the nodes
        return str(self.top.data)

    def push(self, value):
        # to push node we first make the next the of our node refer to the node we want to push then we assign the to to our node 
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        # to pop we first assign the top to the next of our node and then we delete the node, but we have to check if the stack is empty first
        if self.top is None:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        # to peek we just return the top node
        if self.is_empty():
            return "Peeking from an empty stack"
        return self.top.data

    def is_empty(self):
        # to check if the stack is empty we check if the top is none
        return self.top is None   


class PseudoQueue:
    """making a pseudo queue using two stack objects"""
    def __init__(self):
        self.stack1 = Stack() # for pushing
        self.stack2 = Stack() # for popping

    def enqueue(self, value):
        """Push nodes to stack one"""
        self.stack1.push(value)
    
    def dequeue(self):
        """pop from stack two"""
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

if __name__ =="__main__":
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())