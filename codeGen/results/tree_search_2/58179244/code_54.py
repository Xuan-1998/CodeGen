from collections import deque

def solve():
    n = int(input())
    colors = list(input())

    dp = [[0] * 3 for _ in range(n + 1)]
    prev_colors = [''] * (n + 1)

    for i in range(1, n + 1):
        if colors[i - 1] == 'R':
            dp[i][0] = dp[i - 1][1]
            prev_colors[i] = 'G'
            dp[i][2] = dp[i - 1][1] + 1
            prev_colors[i] = 'B'
        elif colors[i - 1] == 'G':
            dp[i][1] = dp[i - 1][0]
            prev_colors[i] = 'R'
            dp[i][2] = dp[i - 1][2] + 1
            prev_colors[i] = 'B'
        else:
            dp[i][2] = dp[i - 1][0]
            prev_colors[i] = 'R'
            dp[i][1] = dp[i - 1][2] + 1
            prev_colors[i] = 'G'

    r, t = dp[-1][1], ''
    for i in range(n):
        if prev_colors[i + 1] == 'G':
            t += 'R' if colors[i] == 'B' else 'G'
        elif prev_colors[i + 1] == 'R':
            t += 'G' if colors[i] == 'B' else 'R'
        else:
            t += 'B' if colors[i] == 'G' else 'B'

    print(r)
    print(t)

solve()
