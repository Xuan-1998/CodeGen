from collections import deque

def max_beauty(n, m, edges):
    dp = [[[float('-inf')] * (m+1) for _ in range(m)] for _ in range(n+1)]

    # Base case: when there are no more edges to consider
    for i in range(1, n+1):
        dp[i][0][0] = 0

    # Fill up the 3D array in a bottom-up manner
    for i in range(1, n+1):
        for j in range(m):
            for k in range(j+1, m):
                if edges[j][0] == i-1 and edges[k][0] != i:
                    # Consider extending the tail or adding an edge as a spine
                    dp[i][j][k] = max(dp[i-1][j-1][k-1], dp[i-1][j][k-1])
                elif edges[j][0] == i and edges[k][0] != i:
                    # Edge j belongs to the tail, edge k is a spine
                    dp[i][j][k] = max(dp[i][j-1][k-1], dp[i][j][k-1])

    return dp[n][m-1][m-1]

# Read input from stdin
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

print(max_beauty(n, m, edges))
