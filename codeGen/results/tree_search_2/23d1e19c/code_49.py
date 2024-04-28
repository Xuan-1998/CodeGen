import heapq

def min_recomputations(graph, path):
    n = len(graph)
    dp = [0] * (n + 1)
    
    for i in range(1, n):
        j = path[i - 1]
        dp[i] = max(dp[j] + 1, dp[i - 1] + 1 if i - 1 != j else 1)
        
    return dp[-1], dp[0]

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
    
    min_recomp, max_recomp = min_recomputations(graph, path)
    
    print(min_recomp, max_recomp)

if __name__ == "__main__":
    main()
