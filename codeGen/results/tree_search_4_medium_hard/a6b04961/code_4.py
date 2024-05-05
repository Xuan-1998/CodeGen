import sys

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = sum(e[2] for e in edges if e[0] == i)

    for length in range(2, n + 1):
        for v in range(1, n - length + 2):
            max_beauty = 0
            for u in range(v - 1, v - length, -1):
                max_beauty = max(max_beauty, dp[length - 1][u] + sum(e[2] for e in edges if e[0] == v and e[1] != u))
            dp[length][v] = max_beauty

    return max(dp[i][i] for i in range(1, n + 1))

print(solve())
