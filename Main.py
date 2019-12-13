from graph_al import GraphAL


def kru(graph):
    sorted_edges = []

    for lst in graph:
        for edge in lst:
            sorted_edges.append(edge)

    sorted_edges.sort(key=lambda e: e.weight)  # sort by weight
    t = GraphAL(6, weighted=True, directed=False)

    for edge in sorted_edges:
        if not t.contains_cyle():
            t.insert_edge(edge.source, edge.dest, edge.weight)

    return t


def topological_sort(graph):
    all = graph.compute_indegree()
    sort_result = []

    q = []

    for i in range(len(all)):
        if all[i] == 0:
            q.append(i)

    while len(q) > 0:
        u = q.pop()

        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all[adj_vertex] -= 1

            if all[adj_vertex] == 0:
                q.append(adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result

# lab 7 solution
def edit_distance(str1, str2):
    dm = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0:
                dm[i][j] = j

            elif j == 0:
                dm[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dm[i][j] = dm[i - 1][j - 1]

            else:
                dm[i][j] = 1 + min(dm[i][j - 1],      # Insert
                                   dm[i - 1][j],      # Remove
                                   dm[i - 1][j - 1])  # Replace

    return dm[-1][-1]


str_one = "treats"
str_two = "tarts"

print(edit_distance(str_one, str_two))
print()

g = GraphAL(6, weighted=True, directed=True)
g.insert_edge(0, 1, 6)
g.insert_edge(0, 2, 7)
g.insert_edge(1, 2, 8)
g.insert_edge(2, 3, 9)
g.insert_edge(3, 4, 5)
g.insert_edge(4, 1, 1)
g.display()

k = kru(g.al)
k.display()

print(topological_sort(g))
