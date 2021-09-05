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
        if not self.head: 
             self.head = node 
        else: 
            node.next = self.head 
            self.head = node


    ##############################
    ######code challenge 06#######
    ##############################

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
    

    ##############################
    ######code challenge 07#######
    ##############################
    def getKthNodeFromEnd(self, k):
        if k < 0:
            return "K is negative"
        node_num = 0
        current = self.head
        while current: # count the nodes 
            current = current.next
            node_num = node_num + 1

        if node_num >= k:
            current = self.head # reset the current value to start the count from the beggining node
            for i in range(node_num - k-1): #k-1 to remove null 
                current = current.next
        else:
            return "Number of K is bigger than the number of Nodes !!!"      
        return current


    ##############################
    ######code challenge 08#######
    ##############################
    def zip_list(self,list1=None, list2=None):
        """
        zip two linked list together
        """
        # we have 6 cases in this code challenge:

        #1- if one of the list is empty, then return the other list 
        #2- if both list are not empty, then return the zipped list
        #3- if both list is empty, then return None
        #4- if the first list is longer
        #5- if the second list is longer
        #6- if the boht linked list same length

        # if both list is not empty => assign pointers and next value
        if list1.head and list2.head:
            temp1=list1.head.next
            temp2=list2.head.next
            list1.head.next=list2.head
            current = list1.head.next

            while(current.next and temp1 and temp2):
                current.next = temp1
                current = current.next
                temp1= current.next

                current.next = temp2
                current=current.next
                temp2= current.next

            while temp1:
                current.next = temp1
                current = current.next
                temp1 = current.next

            while temp2:
                current.next = temp2
                current = current.next
                temp2 = current.next

            return list1

        else:
            if list1.head:
                return list1
            elif list2.head:
                return list2
            else:
                return None


    ##############################
    ######code challenge 09#######
    ##############################
    # write afunction that takes alinked list then return the reverse of that linked list
    def reverse_linked_list(self):
        """write afunction thats takes alinked list then return the reverse of that linked list"""
        
        current = self.head
        if current ==None:
            return "list is empty"
        newll = LinkedList()
        while current: # count the nodes 
            newll.insert(current.value)
            current = current.next
        return newll    