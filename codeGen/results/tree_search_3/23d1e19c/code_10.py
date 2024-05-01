from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    
    k = int(stdin.readline())
    path = list(map(int, stdin.readline().split()))
    
    dp = [float('inf')] * (n+1)
    for i in range(k):
        dp[path[i]] = 0
    
    for i in range(1, n+1):
        if i not in graph:
            continue
        for j in range(i-1, -1, -1):
            if i in graph[j]:
                dp[i] = min(dp[i], dp[j]+1)
    
    print(min(dp), max(dp))

if __name__ == "__main__":
    solve()
