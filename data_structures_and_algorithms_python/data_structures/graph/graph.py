from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) # O(1)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []

        return node

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        if end_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        adjacencies = self.adjacency_list[start_node]
        adjacencies.append((end_node, weight))

    def get_nodes(self):
        return self.adjacency_list.keys()


    def size(self):
        return len(self.adjacency_list)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def bfs(self, start_node):
        nodes = []  
        visited = set()
        breadth = Queue()
        breadth.enqueue(start_node)
        visited.add(start_node)
        while len(breadth)>0: 
            node = breadth.dequeue() 
            nodes.append(node) 
            for n in self.adjacency_list[node]: 
                if n not in visited: 
                    breadth.enqueue(n) 
                    visited.add(n)
        return nodes

    def isPathBFS(self, from_node, to_node):
        queue = []
        visited = []
        queue.append(from_node)
        visited.append(from_node)

        while(queue != []):
            dequeued = queue.pop(0)

        for neighbor in self.get_neighbors(dequeued):
            if neighbor[0] == to_node:
                return True

            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

        return False


if __name__ == "__main__":
    graph = Graph()
    n1 = graph.add_node(1)
    n2 = graph.add_node(2)
    graph.add_edge(n1, n2)
    print(graph.isPathBFS(n1, n2))
    print(graph.isPathBFS(n2, n1))


