import sys

def solve(n, m, h, s):
    if n > sum(s) or n < 1:
        return -1.0
    dp = [[0.0 for _ in range(n+1)] for _ in range(h+1)]

    for i in range(1, h+1):
        dp[i][0] = (s[i-1] / sum(s)) ** n

    for j in range(1, n+1):
        for i in range(h, -1, -1):
            if j >= s[i-1]:
                dp[i][j] = max(dp[i][j-1], (s[i-1] / sum(s)) * ((dp[max(i-1, 0)][j-s[i-1]] if j > s[i-1] else 0.0) + dp[i][j-1]))
            else:
                dp[i][j] = dp[i][j-1]

    return dp[h][n]

input_line = input().split()
n, m, h = map(int, input_line[:3])
s = list(map(int, input_line[3:]))
print('%.6f' % solve(n, m, h, s))
