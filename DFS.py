visited = set()

def dfs(graph, start) :
    print(start)
    visited.add(start)
    for neighbor in graph[start] :
        if neighbor not in visited :
            dfs(graph, neighbor)    


graph = {
    'A': ['F', 'C'],
    'B': ['E', 'D'],
    'C': ['A', 'F', 'B'],
    'D': ['A'],
    'E': ['D', 'F'],
    'F': ['C', 'A']
}

dfs(graph, 'A')