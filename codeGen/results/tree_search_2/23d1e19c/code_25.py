def min_max_recomputation(n, m, edges, k, path):
    # Initialize dp array with all values set to (0, 0)
    dp = [[[0, 0] for _ in range(2**k)] for _ in range(n)]

    # Iterate over each edge and update the dp array
    for u, v in edges:
        for mask in range(2**k):
            if not ((path[u-1] & (1 << k)) >> (k - 1)):
                dp[v][mask][0] = min(dp[v][mask][0], dp[u][mask][0] + 1)
                dp[v][mask][1] = max(dp[v][mask][1], dp[u][mask][1] + 1)

    # Find the minimum and maximum number of recomputations
    min_recomputation = float('inf')
    max_recomputation = 0
    for i in range(2**k):
        min_recomputation = min(min_recomputation, dp[path[-1]][i][0])
        max_recomputation = max(max_recomputation, dp[path[-1]][i][1])

    return min_recomputation, max_recomputation

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

min_recomputation, max_recomputation = min_max_recomputation(n, m, edges, k, path)
print(min_recomputation, max_recomputation)
