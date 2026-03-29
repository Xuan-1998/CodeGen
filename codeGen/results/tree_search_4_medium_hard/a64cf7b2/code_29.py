import sys

def solve():
    n, m, T = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    dp = [0] * (n + 1)
    dp[n] = 1

    for edge in sorted(edges, reverse=True):
        u, v, t = edge
        dp[v] = max(dp[v], dp[u] - t)

    return str(max(dp[1:])), ' '.join(map(str, [i for i in range(2, n + 1) if dp[i]]))

if __name__ == "__main__":
    print(*solve(), sep='\n')
