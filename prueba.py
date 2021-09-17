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


class AStar:
    def __init__(self):
        init = 'A'
        finish = 'I'
        openList = NodeList()
        closeList = NodeList()
        startNode = Node(init)
        openList.append(startNode)
        endNode = None

        while True:
            print(openList)
            if openList == []:
                print("No existe ninguna ruta para llegar al destino.")
                exit(1)
            n = min(openList, key=lambda x: x.fs)
            openList.remove(n)
            closeList.append(n)
            if n.city == endNode:
                endNode = n
                break
            n_gs = n.fs - n.hs
            for city, distance in connects[cities[n.city]]:
                cityB = city
                m = openList.find(cityB)
                dist = distance
                if m:
                    if m.fs > n_gs + m.hs + dist:
                        m.fs = n_gs + m.hs + dist
                        m.parent_node = n
                else:
                    m = closeList.find(cityB)
                    if m:
                        if m.fs > n_gs + m.hs + dist:
                            m.fs = n_gs + m.hs + dist
                            m.parent_node = n
                            openList.append(m)
                            closeList.remove(m)
                    else:
                        m = Node(cityB)
                        m.fs = n_gs + m.hs + dist
                        m.parent_node = n
                        openList.append(m)
        n = endNode
        sol = []
        while True:
            city, distance = n
            sol.append()
            if n.parent_node == None:
                break
            n = n.parent_node
        sol.reverse()
        print(list(sol))


data = AStar()
