import sys
from collections import deque, defaultdict

def shortest_path_recomputations():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))
    
    # Create a graph from the given edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # Initialize memoization table
    memo = {}
    
    def min_max_recomputations(s, t, path):
        if (s, path) not in memo:
            if s == t:
                return [0, 0]
            min_recomputations = float('inf')
            max_recomputations = 0
            for neighbor in graph[path[-1]]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    recomputations = min_max_recomputations(neighbor, t, new_path)
                    min_recomputations = min(min_recomputations, recomputations[0] + 1)
                    max_recomputations = max(max_recomputations, recomputations[1] + 1)
            memo[(s, path)] = [min_recomputations, max_recomputations]
        return memo[(s, path)]
    
    min_max_recomputations(path[0], path[-1], path)

