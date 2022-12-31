def bfs(graph, node):
    visited = {}  # hashing to keep track of visited nodes.
    queue = []

    visited[node] = 1
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited[neighbour] = 1
                queue.append(neighbour)

# O(V+E)
# V = number of vertices
# E = number of edges
