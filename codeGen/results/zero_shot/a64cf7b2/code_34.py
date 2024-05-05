from io import StringIO

def solve():
    n, m, T = map(int, input().split())
    weights = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        weights.append((u, v, t))

    # Initialize the dp table
    dp = [0] * (n + 1)

    for u, v, t in weights:
        dp[v] = max(dp[v], dp[u] + (t <= T))

    max_vertices = dp[n]

    print(max_vertices)

    # Find the vertices that can be visited on the route from 1 to n
    visited_vertices = []
    curr_vertex = n
    while curr_vertex > 0:
        if dp[curr_vertex] == dp[curr_vertex - 1]:
            curr_vertex -= 1
        else:
            visited_vertices.append(curr_vertex)
            curr_vertex -= 1

    print(*visited_vertices[::-1], sep=' ')

if __name__ == '__main__':
    solve()
