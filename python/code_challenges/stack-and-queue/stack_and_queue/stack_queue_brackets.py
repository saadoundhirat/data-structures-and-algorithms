###############################################
##############code challenge 13################
###############################################

# write a function to that takes astring and that includes brackets and return true if the brackets are balanced and false if they are not.
# for example: if the string is "((5+3)*(9-7))" then the function should return true.
# if the string is "(((3+1)+2)*3)" then the function should return false.
# we have three types of brackets () {} [];

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


def match_brackets(string):
    if string == ')':
        return '('
    elif string == ']':
        return '['
    elif string == '}':
        return '{'

def validate_brackets(string):
    "function to validate bracket that takes a string and return true if brackets arebalanced correctly and false if brackets are not balanced correctly"
    # make stack to store the opening brackets
    stack = Stack()
    length_str = len(string)
    for i in range(length_str):
        # check if the current character is an opening bracket
        if str(string[i]) == '(' or string[i] == '{' or string[i] == '[':
            # if it is push it to the stack
            stack.push(string[i])
        elif str(string[i]) == ')' or string[i] == '}' or string[i] == ']':
            # if it is a closing bracket check if the stack is empty
                if stack.is_empty():
                    return False
                elif  stack.peek() == str(match_brackets(string[i])):
                    stack.pop()
                else:
                    pass 
        else:
            pass
    if stack.is_empty():
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(validate_brackets("[stack]"))
    print(validate_brackets("[stack]}"))
    print(validate_brackets("[()+()+{}stack]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("{}{Code}[Fellows](())"))