# This is the solution for code challenge 05 && 06




class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
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


    def include(self, value):
        """Indicates whether that value exists as a Node’s value somewhere within the list."""
        node = self.head # start at the head
        while node: #if node is not None means the end of the list
            if node.value == value:
                return True
            node = node.next # move to next node
        return False

    def insert(self, value):
        """insert anode to the linked list with  Big O(1) so that means we have to add to the beginning of the list"""
        node = Node(value)
        node.next = self.head
        self.head = node

    ##SOLVING lAB 06

    # adds a new node with the given value to the end of the list
    def append(self, value):
        """add a node to the end of the list"""
        node = Node(value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
            node.next = None
        else:
            self.head = node
            node.next = None    

    #adds a new node with the given new value immediately before the first node that has the value specified
    def insert_before(self, targetValue, value):
        """add new node before given node value immediately"""
        found_flag=False
        new_node=Node(value)
        current=self.head
        if current == None:
           raise Exception('LL is empty')
        else:
            while current:
                if current.next == None:
                    if current.value==targetValue:
                        found_flag=True
                        new_node.next = current
                        self.head = new_node
                        break
                if current.next.value==targetValue:
                   found_flag=True
                   new_node.next=current.next
                   current.next=new_node
                   break
                else:
                  current=current.next
            if found_flag !=True:
               print('Targeted value not found')
    

    #adds a new node with the given new value immediately after the first node that has the value specified
    def insert_after(self, value, new_value):
        if not self.head:
            raise Exception("the ll is empty")
        found_flag = False
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                found_flag=True
                break
            current = current.next

        if not found_flag:
            raise Exception ("the key is not found")


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.insert_before(6,4)
    print(ll)