from typing import DefaultDict


class Edge(object):
    def __init__(self, cityB, distance):
        self.cityB = cityB
        self.distance = distance


class Node(object):
    def __init__(self, city):
        self.city = city
        self.hs = h[city]
        self.fs = 0
        self.parent_node = None


class NodeList(list):
    def find(self, city):
        l = [t for t in self if t.city == city]
        return l[0] if l != [] else None

    def remove(self, node):
        del self[self.index(node)]


cities = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
          'I': 8}

connects = [
    [('B', 3), ('F', 7), ('C', 4)],
    [('A', 2), ('H', 6)],
    [('A', 4), ('H', 3), ('D', 5)],
    [('C', 5), ('H', 2), ('F', 7), ('G', 2), ('I', 12)],
    [('F', 4), ('I', 6)],
    [('A', 7), ('I', 16), ('D', 7), ('E', 4)],
    [('H', 1), ('D', 2), ('I', 5)],
    [('B', 6), ('C', 3), ('D', 2), ('G', 1)],
    [('G', 5), ('D', 12), ('F', 16), ('E', 6)]
]

h = {'A': 7, 'B': 5, 'C': 6, 'D': 3, 'E': 5, 'F': 8, 'G': 4,
     'H': 4, 'I': 0}



class Graph:
 
    def __init__(self):
 
        self.graph = DefaultDict(list)
 
    def addNode(self,u,v):
        self.graph[u].append(v)
 


def bfs(matrix, starting_node):
    visited = []
    c_nodos = [starting_node]
    
    while c_nodos:
        node = c_nodos.pop(0)
        if node not in visited:
            visited.append(node)            
            for edge in matrix:
                for i in edge:
                    if(i < len(edge)):
                        if edge[i] == node:
                            c_nodos.append(edge[i+1])
                        elif edge[i+1] == node:
                            c_nodos.append(edge[i])
    return visited
