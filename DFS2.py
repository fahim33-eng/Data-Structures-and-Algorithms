def dfs(graph, start) :
    visited = set()
    stack = [start]
    
    while stack :
        node = stack.pop()
        if node not in visited :
            print(node)
            visited.add(node)
        
        for neighbor in reversed(graph[node]) :
            if neighbor not in visited :
                stack.append(neighbor)



graph = {
    'A': ['F', 'C'],
    'B': ['E', 'D'],
    'C': ['A', 'F', 'B'],
    'D': ['A'],
    'E': ['D', 'F'],
    'F': ['C', 'A']
}

dfs(graph, 'A')