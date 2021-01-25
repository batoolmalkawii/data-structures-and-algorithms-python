from data_structures_and_algorithms_python.data_structures.graph.graph import Graph, Node, Queue


def to_nodes_dict(nodes):
    nodes_dict = {}
    for node in nodes:
        nodes_dict[node.value] = node
    return nodes_dict

def to_neighbors_dict(nodes):
    neighbors = {}
    for node in nodes:
        neighbors[node[0].value] = node
    return neighbors

def get_edge(graph, arr):
    price = 0
    nodes = graph.get_nodes()
    nodes_dict = to_nodes_dict(nodes)

    for i in range (0, len(arr)-1):

        if arr[i] not in nodes_dict:
            return False, '$0'

        if arr[i] in nodes_dict:
            neighbors = graph.get_neighbors(nodes_dict[arr[i]])
            neighbors_dict = to_neighbors_dict(neighbors)

            if arr[i+1] in neighbors_dict:
                price += neighbors_dict[arr[i+1]][1]

            else:
                return False, '$0'

    return True, f'${price}'
