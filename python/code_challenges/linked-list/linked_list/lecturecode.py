class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    # we have to use magic method here because when need to have string to represent the value of the node when we print it.
    def __str__(self):
        return self.value

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def insert(self ,value):
        # method body here
        new_node = Node(value)
        # to make the head point to the new node if the head was None
        if self.head == None:
              self.head = new_node
        #else if the head is not None
        else:
            # if the linked list already having and items so we have to jump to the last node using while then we change next to null and the current to the node we want
            current= self.head
            while current.next: # if next != none jump to the next node
                current = current.next

            current.head = new_node # to make the last node

    # make astring representation to the linked list values, so we have to use magic methods __str__ here 1=> 2=> 3 to the end of the linked list
    def __str__(self):
        # 1- create new string to be returned
        output_string = "Linked_List=>>>"
        # 2- eterate over each node to get there values
        # note that to point over the list we have to get acurrent value start point and the move to the next node
        current = self.head
        while current:
        # 3- append the value to the string output
            output_string+= f"{str(current.value)}=>"
        # 4- after we append the value to the string we have to move to the next node
            current = current.next
        # 5- return the output string
        output_string += "None"
        return output_string
    # this function used to iterrate over the kinked list of nodes and return alist include all nodes
    def __iter__(self):
        # output_list =[]
        current = self.head
        while current:
            yield current.value
            current = current.next
        # return iter(output_list)

    def __repr__(self):
        return 'Linked_List()'

# to test the linked list
if __name__ == '__main__':
    node = Node("saadoun")
    print(node)
    linked_list = LinkedList()
    linked_list.head =node
    print(linked_list.head)

#  to test the __str__ to see if its print each node in the linked list
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    print(ll)

#  this to work with the __add__ method
    # node1= Node(1)
    # node2= Node(2)
    # node3= Node(1) + Node(2)


    for value in ll:
        print(value)
