graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def DFS (graph, start):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            queue.extend(reversed(graph[node]))



print(graph)
DFS(graph, 'A')

