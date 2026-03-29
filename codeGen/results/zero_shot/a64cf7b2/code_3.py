import sys

def solve(n, m, T):
    # Read edges from stdin
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v, t))

    # Create dp table
    dp = [[0] * (T + 1) for _ in range(n + 1)]

    # Initialize dp table
    dp[0][0] = 1

    # Fill up the dp table
    for u, v, t in edges:
        for i in range(T, -1, -1):
            if dp[u][i] and i >= t:
                dp[v][min(i, T)] += 1

    # Find the maximum number of vertices that can be visited
    max_vertices = 0
    for i in range(1, n + 1):
        max_vertices = max(max_vertices, dp[i][T])

    # Print the result
    print(max_vertices)
    for i in range(max_vertices - 1, -1, -1):
        v = n
        while dp[v][T] > i:
            v -= 1
        print(v + 1)

if __name__ == "__main__":
    n, m, T = map(int, sys.stdin.readline().split())
    solve(n, m, T)
