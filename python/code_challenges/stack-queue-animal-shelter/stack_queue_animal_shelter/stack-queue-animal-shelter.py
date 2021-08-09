class Dog:
    def __init__(self):
        self.name = "dog"
        self.next= None
    def __str__(self):
        return str(self)

class Cat:
    def __init__(self):
        self.name = "cat"
        self.next= None
    def __str__(self):
        return str(self.name)

class AnimalShelter:
    def __init__(self):
        self.front= None
        self.rear= None

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
        if value == 'cat' or value = "dog ":
            node = 