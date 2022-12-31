visited = set()  # Set to keep track of visited nodes.
def dfs(visited,graph, node):

    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
