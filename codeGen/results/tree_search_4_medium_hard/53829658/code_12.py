import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    graph = {}
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    return n, graph

def solve():
    n, graph = read_input()
    dp = [[False] * (n + 1) for _ in range(n)]

    # Initialize DP table
    for i in range(1, n):
        if not any(dp[i-1][j] and j != i for j in graph.get(i, [])):
            dp[i][i] = True

    # Update DP table using edges
    for u in graph:
        for v in graph[u]:
            for k in range(n - 1, 0, -1):
                if not dp[u][k-1] or dp[v][k-1]:
                    dp[v][k] = True
                    break

    # Calculate minimum number of reversed edges
    min_edges = max(k for k in range(n) if any(dp[n-1][k]) and k > 0)

    return min_edges, [i+1 for i in range(n) if dp[n-1][n-1]]

def main():
    min_edges, cities = solve()
    print(min_edges)
    print(*cities, sep='\n')

if __name__ == "__main__":
    main()
