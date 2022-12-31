def bfs(graph, node):
    visited = [] # List to keep track of visited nodes.
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
       for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(graph, 'A')

# O(V+E)
# V = number of vertices
# E = number of edges
