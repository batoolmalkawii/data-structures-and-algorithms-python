from data_structures_and_algorithms_python.data_structures.graph.graph import Graph, Node, Queue
from data_structures_and_algorithms_python.data_structures.graph.get_edges.get_edges import get_edge, to_neighbors_dict, to_nodes_dict
import pytest

def test_to_nodes_dict():
    graph = Graph()

    amman = graph.add_node("amman")
    zarqa = graph.add_node("zarqa")
    irbid = graph.add_node("irbid")
    salt = graph.add_node("salt")
    aqaba = graph.add_node("aqaba")
    damanhur = graph.add_node("damanhur")

    graph.add_edge(amman, irbid, 150)
    graph.add_edge(amman, zarqa, 82)
    graph.add_edge(irbid, zarqa, 99)
    graph.add_edge(zarqa, salt, 105)
    graph.add_edge(irbid, salt, 42)
    graph.add_edge(zarqa, aqaba, 37)
    graph.add_edge(zarqa, damanhur, 26)
    graph.add_edge(damanhur, damanhur, 250)
    graph.add_edge(salt, damanhur, 73)

    nodes_dict = to_nodes_dict(graph.get_nodes())

    assert nodes_dict == {
                            "amman": amman,
                            "zarqa": zarqa,
                            "irbid": irbid,
                            "salt": salt,
                            "aqaba": aqaba,
                            "damanhur": damanhur
                            }

def test_to_nodes_dict_empty():
    graph = Graph()
    nodes_dict = to_nodes_dict(graph.get_nodes())
    assert nodes_dict == {}

def test_to_neighbors_dict():
    graph = Graph()

    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    graph.add_edge(a, b, 150)
    graph.add_edge(a, c, 100)
    graph.add_edge(a, d, 50)

    neighbors_dict = to_neighbors_dict(graph.get_neighbors(a))

    assert neighbors_dict == {
                            "b":(b, 150),
                            "c":(c, 100),
                            "d":(d, 50),
                            }

def test_to_neighbors_dict_no_neighbors():
    graph = Graph()
    a = graph.add_node("a")
    neighbors_dict = to_neighbors_dict(graph.get_neighbors(a))
    assert neighbors_dict == {}

def test_two_direct_cities(my_graph):
    graph = my_graph
    assert get_edge(graph, ['amman', 'zarqa']) == (True, '$82')

def test_two_non_direct_cities(my_graph):
    graph = my_graph
    assert get_edge(graph, ['damanhur', 'amman']) == (False, '$0')

def test_city_not_in_graph(my_graph):
    graph = my_graph
    assert get_edge(graph, ['zarqa', 'amman', 'Kazan']) == (False, '$0')


@pytest.fixture
def my_graph():
    graph = Graph()
    amman = graph.add_node("amman")
    zarqa = graph.add_node("zarqa")
    irbid = graph.add_node("irbid")
    salt = graph.add_node("salt")
    aqaba = graph.add_node("aqaba")
    damanhur = graph.add_node("damanhur")

    graph.add_edge(amman, irbid, 150)
    graph.add_edge(amman, zarqa, 82)
    graph.add_edge(irbid, zarqa, 99)
    graph.add_edge(zarqa, salt, 105)
    graph.add_edge(irbid, salt, 42)
    graph.add_edge(zarqa, aqaba, 37)
    graph.add_edge(zarqa, damanhur, 26)
    graph.add_edge(damanhur, damanhur, 250)
    graph.add_edge(salt, damanhur, 73)

    return graph