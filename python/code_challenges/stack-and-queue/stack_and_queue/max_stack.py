###############################################
##############code challenge 14################
###############################################

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
        """pop from stack"""
        if not self.top:
            return "stack is empty"
        else:
            data=self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        # to peek we just return the top node
        if self.is_empty():
           return "Peeking from an empty stack"
        return self.top.data

    def is_empty(self):
        # to check if the stack is empty we check if the top is none
        return self.top is None   


    def maxStack(self):
        """function that return the max_stack value"""
        if self.is_empty():
            return "Empty Stack"
        max_value = self.top.data
        while self.top.next is not None:
            self.top = self.top.next
            if self.top.data > max_value:
                max_value = self.top.data
        return max_value


if __name__ =="__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.maxStack())