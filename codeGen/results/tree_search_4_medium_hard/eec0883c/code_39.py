import sys

def read_input():
    n = int(input())
    w = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i], *_ = map(int, input().split())

    edges = []
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))

    return n, w, edges

def solve(n, w, edges):
    # Initialize the dynamic programming table
    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]

    # Fill up the base case
    for i in range(1, n + 1):
        dp[i][w[i]] = w[i]

    # Process each edge
    for u, v, c in edges:
        for j in range(min(w[u], w[v] + c), -1, -1):
            dp[v][j] = max(dp[v][j], min(dp[u][j], w[v] - c))

    return dp[0][w[0]]

if __name__ == "__main__":
    n, w, edges = read_input()
    print(solve(n, w, edges))
