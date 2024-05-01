import sys

def shortest_path_recomputation(n, m, graph, k, path):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    recomputations = [0] * n

    # Base case: at vertex t, no more recomputation needed
    for i in range(k - 1, -1, -1):
        if graph[path[i]][path[i + 1]] == 1:
            recomputations[i] = min(max(recomputations[i], dp[path[i]][path[i + 1]]) + 1, max(recomputations[i], dp[path[i + 1]][t]) + 1)

    # Update dp[u][v]
    for i in range(k - 1, -1, -1):
        if graph[path[i]][path[i + 1]] == 1:
            dp[path[i]][path[i + 1]] = min(max(dp[path[i]][path[i + 1]], recomputations[i] + 1), max(dp[path[i]][path[i + 1]], recomputations[i + 1] + 1))

    return dp[0][t - 1]

# Read input
n, m = map(int, sys.stdin.readline().split())
graph = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
k = int(sys.stdin.readline())
path = list(map(int, sys.stdin.readline().split()))

print(shortest_path_recomputation(n, m, graph, k, path))
