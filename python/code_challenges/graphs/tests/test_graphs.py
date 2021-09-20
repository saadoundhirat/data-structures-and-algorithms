import pytest
from graphs import __version__
from graphs.graph import Graph, Vertex

def test_version():
    assert __version__ == '0.1.0'


def test_add_node():

    graph = Graph()

    expected = 'spam'  # a vertex's value that comes back

    actual = graph.add_node('spam').value

    assert actual == expected


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

# test code challenge 36
def test_breadth_search():
    graph = Graph()
    node1 = graph.add_node('Pandora')
    node2 = graph.add_node('Aredelle')
    node3 = graph.add_node('Metroville')
    node4 = graph.add_node('Monstarpolis')
    node5 = graph.add_node('Narina')
    node6 = graph.add_node('Naboo')

    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node4)
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)
    graph.add_edge(node4, node6)

    assert graph.breadth_search(node1) == ['Pandora', 'Aredelle', 'Metroville', 'Monstarpolis', 'Narina', 'Naboo']

def test_business_trip():
    graph = Graph()
    v1 = graph.add_node('Pandora')
    v2 = graph.add_node('Arendelle')
    v3 = graph.add_node('Metroville')
    v4 = graph.add_node('Monstropolis')
    v5 = graph.add_node('Narnia')
    v6 = graph.add_node('Naboo')
    graph.add_edge(v1,v2,150)
    graph.add_edge(v1,v3,82)
    graph.add_edge(v2,v3,99)
    graph.add_edge(v2,v4,42)
    graph.add_edge(v3,v4,105)
    graph.add_edge(v3,v5,37)
    graph.add_edge(v3,v6,26)
    graph.add_edge(v4,v6,73)
    graph.add_edge(v5,v6,250)
    cities = [v1,v2,v3]
    assert graph.business_trip(cities) == (True, '$249')

def test_graph_depth_first():
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
    values = graph.depth_first(v1)
    actual = [vertex.value for vertex in values]
    assert actual == ['a', 'b', 'a', 'd', 'e', 'h', 'f', 'c', 'g']