from dsf import DisjointSetForest


class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight


class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(source, dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(dest, source, weight))

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def contains_cyle(self):  # Asumption: Directed Graph
        dsf = DisjointSetForest(self.num_vertices())

        for i in range(len(self.al)):
            for edge in self.al[i]:
                if dsf.find(i) == dsf.find(edge.dest):
                    return True

                dsf.union(i, edge.dest)

        return False

    def display(self):
        print('[', end='')
        for i in range(len(self.al)):
            print('[', end='')
            for edge in self.al[i]:
                print('(' + str(edge.dest) + ',' + str(edge.weight) + ')', end='')
            print(']', end=' ')
        print(']')

    def compute_indegree(self):
        ind = [0] * self.num_vertices()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                if edge.weight == i:
                    ind[i] += 1

        return ind
