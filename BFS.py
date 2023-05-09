visited = set()
queue = []
    
def bfs(graph, start) :
    queue.append(start)
    while queue :
        node = queue.pop(0)
        if node not in visited :
            visited.add(node)
            print(node)
            for neighbor in graph[node] :
                if neighbor not in visited :
                    queue.append(neighbor)
                    

graph = {
    'A': ['F', 'C'],
    'B': ['E', 'D'],
    'C': ['A', 'F', 'B'],
    'D': ['A'],
    'E': ['D', 'F'],
    'F': ['C', 'A']
}


bfs(graph, 'A')