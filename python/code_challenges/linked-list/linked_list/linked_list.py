# This is the solution for code challenge 05

# node class for linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        """initialization here"""
        self.head = None

    # to return astring value
    def __str__(self):
        """ Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL" """
        current=self.head
        result = ""
        while current:
            result+= f"{str(current.value)}=>"
            current = current.next
        result += "NULL"
        return result

    def __repr__(self):
        return "Linkedlist"

    def insert(self, value):
        """insert anode to the linked list with  Big O(1) so that means we have to add to the beginning of the list"""
        node = Node(value)
        node.next = self.head
        self.head = node

    def include(self, value):
        """Indicates whether that value exists as a Node’s value somewhere within the list."""
        node = self.head # start at the head
        while node: #if node is not None means the end of the list
            if node.value == value:
                return True
            node = node.next # move to next node
        return False


if __name__ == '__main__':
    # node = Node("saadoun")
    # print(node)
    # linked_list = LinkedList()
    # linked_list.head =node
    # print(linked_list.head)

#  to test the __str__ to see if its print each node in the linked list
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    print(ll) # should print: 3=>4=>5=>NULL