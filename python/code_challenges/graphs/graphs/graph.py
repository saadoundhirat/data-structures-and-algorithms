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
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight  = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def print_graph(self):
        print(self._adjacency_list)

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

    def print_adjacency_list(self):
        list = self._adjacency_list.keys()
        for key in list:
            edges = ""
            for childe in self._adjacency_list[key]:
                edges += childe.vertex.value + " => "
            print(key.value, ":",f"{edges}" )

    def get_nodes(self):
        """Get all of the nodes in the graph"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """Get all of the neighbors of a vertex"""
        return self._adjacency_list.get(vertex, [])

    def breadth_first_search_action(self, start_vertex, action=(lambda x: None)):
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
    
    def breadth_search(self, root):
        if root is None:
            return []
        neighbors_list = self.get_neighbors(root)
        if len(neighbors_list) == 0:
            return []
        queue = Queue()
        visited = set() #unique values 
        result_list = []
        
        queue.enqueue(root)
        visited.add(root)

        while len(queue):
            current_vertex = queue.dequeue()
            result_list.append(current_vertex.value)
            for edge in self._adjacency_list[current_vertex]:
                neighbor_vertex = edge.vertex
                if neighbor_vertex not in visited:
                    visited.add(neighbor_vertex)
                    queue.enqueue(neighbor_vertex)
        return result_list

    def business_trip(self,cities:list):

        if len(cities) == 0:
            return False,'$0' 

        if self._adjacency_list[cities[0]] == []:
            return False,'$0' 
        sum = 0
        path_found_flag = False
        for i in range(len(cities)-1):
            neighbors = self._adjacency_list[cities[i]]
            for neighbor in neighbors:
                if cities[i+1].value == neighbor.vertex.value:
                    sum += neighbor.weight
                    path_found_flag = True
                    break
                else:
                    sum += 0
                    path_found_flag = False
        if not path_found_flag:
            return False,'$0'     
        return True,'$'+ str(sum)

    
    def depth_first(self, vertex=None):
        if not vertex:
            return[]
        visited = set()
        nodes = []

        def rec_fun(node):
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                node_v = neighbor.vertex
                if node_v in visited:
                    continue
                else:
                    nodes.append(node_v)
                    visited.add(node_v)
                    rec_fun(node_v)

        nodes.append(vertex)
        rec_fun(vertex)
        return nodes




if __name__ == "__main__":
    # graph = Graph()
    # node1 = graph.add_node('Pandora')
    # node2 = graph.add_node('Aredelle')
    # node3 = graph.add_node('Metroville')
    # node4 = graph.add_node('Monstarpolis')
    # node5 = graph.add_node('Narina')
    # node6 = graph.add_node('Naboo')

    # graph.add_edge(node1, node2)
    # graph.add_edge(node2, node3)
    # graph.add_edge(node2, node4)
    # graph.add_edge(node3, node5)
    # graph.add_edge(node3, node6)
    # graph.add_edge(node4, node6)
    # print(graph.breadth_search(node1))
    # graph = Graph()
    # v1 = graph.add_node('Pandora')
    # v2 = graph.add_node('Arendelle')
    # v3 = graph.add_node('Metroville')
    # v4 = graph.add_node('Monstropolis')
    # v5 = graph.add_node('Narnia')
    # v6 = graph.add_node('Naboo')
    # graph.add_edge(v1,v2,150)
    # graph.add_edge(v1,v3,82)
    # graph.add_edge(v2,v3,99)
    # graph.add_edge(v2,v4,42)
    # graph.add_edge(v3,v4,105)
    # graph.add_edge(v3,v5,37)
    # graph.add_edge(v3,v6,26)
    # graph.add_edge(v4,v6,73)
    # graph.add_edge(v5,v6,250)

    # print(graph.print_adjacency_list())
    # cities = [v1,v2,v3]
    # print(graph.business_trip(cities))
    # cities2 = [v1,v2]
    # print(graph.business_trip(cities2))
    # cities3 = [v6,v1]
    # print(graph.business_trip(cities3))
    # cities4 = [v6]
    # print(graph.business_trip(cities4))


    graph = Graph()
    v1 = graph.add_node('a')
    v2 = graph.add_node('b')
    v3 = graph.add_node('c')
    v4 = graph.add_node('d')
    v5 = graph.add_node('e')
    v6 = graph.add_node('f')
    v7 = graph.add_node('g')
    v8 = graph.add_node('h')
    graph.add_edge(v1, v2)
    graph.add_edge(v1, v4)
    graph.add_edge(v2,v1)
    graph.add_edge(v2,v3)
    graph.add_edge(v2,v4)
    graph.add_edge(v3,v2)
    graph.add_edge(v3,v7)
    graph.add_edge(v4,v1)
    graph.add_edge(v4,v2)
    graph.add_edge(v4,v5)
    graph.add_edge(v4,v8)
    graph.add_edge(v4,v6)
    graph.add_edge(v6,v4)
    graph.add_edge(v6,v8)
    graph.add_edge(v8,v6)
    graph.add_edge(v8,v4)
    graph.add_edge(v5,v4)
    breadth = graph.depth_first(v1)
    actual = [vertex.value for vertex in breadth]
    print(actual)

