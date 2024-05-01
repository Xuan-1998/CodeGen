import sys

def main():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    memo = {i: float('inf') for i in range(n+1)}
    memo[path[0]] = 0
    
    def dp(i):
        if memo[i] != float('inf'):
            return memo[i]
        
        min_recomputations = float('inf')
        for j in range(k-1, -1, -1):
            if has_edge(path[j], i):
                min_recomputations = min(min_recomputations, dp(path[j]) + 1)
        
        memo[i] = min_recomputations
        return min_recomputations
    
    print(dp(path[-1]))

if __name__ == "__main__":
    main()
