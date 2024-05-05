import sys

def solve():
    n, m, T = map(int, input().split())
    dp = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    for u, v, t in edges:
        if dp[u - 1] + t <= T:
            dp[v] = max(dp[v], dp[u - 1] + 1)

    k = max(0, *dp)
    visited = [i + 1 for i in range(n) if dp[i] == k]
    print(k)
    print(*visited, sep='\n')

if __name__ == '__main__':
    solve()
