from collections import deque

class Stack:
    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = deque()

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) -> int:
        return self.stack[-1]  

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)   

    def pop(self) -> None:
        self.stack.pop()

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def __len__(self):
        return len(self.queue)

############################ Lab Solution ############################

class Vertex(): # node
    def __init__(self, value):
        self.value = value 

class Edge():
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight  = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """Adds value to a node and adds the node to a graph"""
        vertex_node = Vertex(value)
        self._adjacency_list[vertex_node] = []
        return vertex_node # we have to return the node so we an have access to it and use value method on it to get the value

    def size(self):
        """return the length of the _adjacency_list """
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight))

    def get_nodes(self):
        """Get all of the nodes in the graph"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """Get all of the neighbors of a vertex"""
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set() # set is a collection of unique elements so we can use it to check if a node has been visited already

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor_vertex = edge.vertex

                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)

if __name__ == "__main__":
    g = Graph()
    node1 = g.add_node('node1')
    node2 = g.add_node('node2')
    g.add_edge(node1, node2)

    g.breadth_first_search(node1, lambda v: print(v.value))