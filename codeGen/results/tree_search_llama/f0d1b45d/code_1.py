from collections import defaultdict

def forest_trees():
    n = int(input())
    ancestors = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if abs(ancestors[i] - ancestors[j]) == 2**j:
                graph[ancestors[i]].append(ancestors[j])
                graph[ancestors[j]].append(ancestors[i])
    
    visited = set()
    trees = 0
    
    def dfs(vertex):
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                dfs(neighbor)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            trees += 1
    
    print(trees)

forest_trees()
