########################
###code challenge 12####
########################
class dog:
    name = "dog"
    def __init__(self):
        self.name = "dog"
        self.next= None
    def __str__(self):
        return str(self)

class cat:
    name = "cat"
    def __init__(self):
        self.name = "cat"
        self.next= None
    def __str__(self):
        return str(self.name)

class AnimalShelter:
    def __init__(self):
        self.front= None
        self.rear= None
    def __str__(self):
        """print the queue"""
        if self.is_empty():
            return "queue is empty"
        else:
            node = self.front
            while node:
                print(node.name)
                node = node.next
            return "None"

    def is_empty(self):
        """if queue is empty"""
        return self.front is None

    def peek(self):
        """peek and return the first node in the queue"""
        if self.is_empty():
            return "queue is empty enqueue to peek"
        else:
            return self.front.name

    def enqueue(self , value):
        """make enqueue function that will only make new node if value is dog or cat """
        if value == 'dog' or value == 'cat':
            if value == 'dog':
                node =  dog()
            if value == 'cat':
                node = cat()

            if not self.rear:
                self.front = node
                self.rear = node
            else:
                self.rear.next = node
                self.rear = node 
        else:
            return "we only add dogs or cats, other animals not allowed"

    def dequeue(self,preference=None):
        """make dequeue function that will return animal based on preference"""
        if self.is_empty():
            return 'animal shelter is empty'
        if self.front.name == preference:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.name
        else:
            temp=self.front
            while self.front.next:
                if self.front.next.name == preference:
                    temp2 = self.front.next
                    self.front.next = self.front.next.next
                    self.front = temp
                    temp2.next = None
                    return temp2.name
                else:
                        self.front = self.front.next
            
            self.front = temp
            return "Your preference not found in the Animal shelter"

if __name__=='__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    print(shelter)
    print(shelter.dequeue('cat'))
    print(shelter.dequeue('dog'))
    print(shelter.dequeue('cat'))
    print(shelter.dequeue('snake'))