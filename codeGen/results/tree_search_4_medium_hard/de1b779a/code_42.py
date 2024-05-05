from collections import namedtuple

State = namedtuple('State', 'dough_left used_stuffs')

def max_profit(n, m, c0, d0, ai, bi, ci, di):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                continue
            if j == 0:
                dp[i][j] = di if i >= d0 else 0
            elif i < c0:
                dp[i][j] = dp[i][0]
            else:
                max_profit = dp[i - c0][j]
                for k in range(j):
                    if ai[k] > 0 and i >= ci[k]:
                        max_profit = max(max_profit, di + dp[i - ci[k]][k])
                dp[i][j] = max_profit

    return dp[n][m]

n, m, c0, d0 = map(int, input().split())
ai, bi, ci, di = [], [], [], []
for _ in range(m):
    ai.append(*map(int, input().split()))

print(max_profit(n, m, c0, d0, *zip(*[list(map(int, input().split())) for _ in range(m)])))
