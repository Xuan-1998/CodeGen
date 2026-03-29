import sys

def solve():
    n, m, T = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, -t))
        graph[v].append((u, t))  # Flip the edge

    dp = [0] * (n + 1)
    parent = [-1] * (n + 1)

    def bellman_ford(u):
        dp[u] = float('-inf')
        for v, w in graph[u]:
            if dp[v] > dp[u] + w:
                dp[v] = dp[u] + w
                parent[v] = u

    bellman_ford(1)
    max_weight = max(dp[1:])
    path = []
    while n != 1:
        v, p = parent[n], n
        for neighbor, weight in graph[p]:
            if neighbor == v and dp[v] - dp[neighbor] + weight > max_weight:
                break
        path.append(v)
        n = v

    print(len(path) + 1)
    print(*reversed(path), sep='\n')

if __name__ == "__main__":
    solve()
