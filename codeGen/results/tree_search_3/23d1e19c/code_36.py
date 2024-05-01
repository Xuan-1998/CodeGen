import sys

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    t = path[-1]
    
    f = [0] * (n+1)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(k-1):
        j = path[i]
        for k in range(j, t+1):
            if has_edge(k, j):
                f[k] = min(f[j] + 1 for j in range(i, t+1) if has_edge(j, k))
    
    return min(max(dp[i]) for i in range(0, t+1))

def has_edge(u, v):
    return v in graph[u]

if __name__ == "__main__":
    print(main())
