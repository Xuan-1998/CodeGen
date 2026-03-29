import sys

def solve():
    n, m, T = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dp = [0] * (n + 1)
    max_vertices = 0

    for i in range(1, n + 1):
        for neighbor, time in graph[i]:
            if time <= T:
                dp[neighbor] = max(dp[neighbor], dp[i] + 1)

    max_vertices = max(dp)
    visited = []
    curr_vertex = n
    while dp[curr_vertex] > 0:
        visited.append(curr_vertex)
        curr_vertex -= 1

    print(max_vertices)
    print(' '.join(map(str, reversed(visited))))

if __name__ == "__main__":
    solve()
