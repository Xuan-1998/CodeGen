import sys

def solve():
    n, m, T = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    # Create a table to store the maximum number of vertices that can be visited
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = 1

    # Iterate over the edges and update the dp table
    for u, v, t in edges:
        for i in range(n, u - 1, -1):  # reverse order to avoid overwriting
            if dp[i] + t <= T:
                dp[i] = max(dp[i], dp[u] + 1)
            if i == n:  # reached the end vertex
                break

    # Find the maximum number of vertices that can be visited
    k = max(dp[1:])
    print(k)

    # Print the indices of vertices that can be visited on the route from vertex 1 to vertex n
    for i in range(n, 0, -1):
        if dp[i] == k:
            print(i)
            break

if __name__ == "__main__":
    solve()
