class Stack_empty(Exception):
    def __init__(self ,*args):
        if args:
            self.message = args
        else:
            return self.message == None
    def __str__(self):
        return "Peeking from an empty stack"
        
class Queue_empty(Exception):
    def __init__(self ,*args):
        if args:
            self.message = args
        else:
            return self.message == None
    def __str__(self):
        return "Peeking from an empty Queue"

class Node:
    def __init__(self, data:None):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

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
            raise Stack_empty("Peeking from an empty stack")
        return self.top.data

    def is_empty(self):
        # to check if the stack is empty we check if the top is none
        return self.top is None   

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # to enqueue we first make the rear the next of our node and then we assign the node to our node
        node = Node(value)
        # If the queue is empty, the new node goes to the front
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        # to dequeue we first check if the queue is empty
        if self.front is None:
            return None
        # if the queue is not empty we first make the front the next of our node and then we delete the node
        value = self.front.data
        self.front = self.front.next
        return value

    def is_empty(self):
        # to check if the queue is empty we check if the front is none
        return  self.front is None

    def peek(self):
        # to peek we just return the front node
        if self.is_empty():
            raise Queue_empty("Peeking from an empty queue")
        return self.front.data

if __name__ == "__main__":
    print("testing Stack")
    stack = Stack()
    # print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.is_empty())
    print(stack.peek())

    print("testing Queue")

    queue = Queue()
    print(queue.peek())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue.peek())
    # to test if its empty
    # print(queue.dequeue())