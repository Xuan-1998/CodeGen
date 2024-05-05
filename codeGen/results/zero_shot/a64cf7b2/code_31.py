import sys

def solve():
    n, m, T = map(int, sys.stdin.readline().split())
    graph = {}
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        if u not in graph: graph[u] = []
        graph[u].append((v, t))

    dp = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)

    dp[1] = 0
    for u in range(2, n + 1):
        for v, t in graph.get(u, []):
            if dp[u] + t <= T and dp[v] < dp[u] + t:
                dp[v] = dp[u] + t
                prev[v] = u

    k = 0
    visited = set()
    for i in range(2, n + 1):
        if dp[i] <= T and i not in visited:
            visited.add(i)
            print(i, end=' ')
            k += 1
    print()

    print(k)

if __name__ == '__main__':
    solve()
