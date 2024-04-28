import sys

def min_max_recomputations(n, m, edges, k, path):
    # Create a 2D array for dp
    dp = [[0, float('inf')] for _ in range(n + 1)]

    # Fill the dp table using dynamic programming with memoization
    for i in range(1, n + 1):
        if i == path[k - 1]:
            continue
        min_recomps, max_recomps = 0, float('inf')
        for j in range(k - 2, -1, -1):
            if edges[path[j] - 1][path[j + 1] - 1]:
                prev_min_recomps, prev_max_recomps = dp[path[j]][1]
                if i != path[j]:
                    min_recomps += 1
                    max_recomps = min(max_recomps, prev_max_recomps)
            else:
                break
        dp[i][0] = min_recomps
        dp[i][1] = max_recomps

    # Print the minimum and maximum number of recomputations
    print(dp[-1][0], dp[-1][1])

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u - 1].append(v)
    edges[v - 1].append(u)
k = int(sys.stdin.readline())
path = list(map(int, sys.stdin.readline().split()))

min_max_recomputations(n, m, edges, k, path)
