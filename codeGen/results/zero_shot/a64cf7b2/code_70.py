import sys

def solve(n, m, T):
    # Read input edges
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v, t))

    # Initialize DP array
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # Fill up the DP array
    for i in range(1, n):
        for j in range(T + 1):
            if j >= edges[i - 1][2]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - edges[i - 1][2]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the maximum number of vertices that can be visited
    k = dp[n - 1][T]
    result = []
    i, j = n - 1, T
    while j > 0 and i > 0:
        if k == dp[i - 1][j]:
            i -= 1
        else:
            result.append(i)
            k -= 1
            j -= edges[i - 1][2]
    return k, result[::-1]

# Read input from stdin
n, m, T = map(int, sys.stdin.readline().split())
print(*solve(n, m, T), sep='\n')
