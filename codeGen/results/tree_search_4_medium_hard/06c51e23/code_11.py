import sys

def max_grade(frac, i, t):
    if i >= len(frac):
        return 0

    digit = int(10 * (frac - int(frac)))
    if digit >= 5:
        return dp[i-1][t-1] + 1
    else:
        return dp[i-1][t-1]

dp = [[0] * (t+1) for _ in range(n+1)]
for i in range(1, n+1):
    for t in range(t, -1, -1):
        if frac[i-1] >= 5:
            dp[i][t] = max(dp[i-1][t-1] + 1, dp[i-1][t])
        else:
            dp[i][t] = dp[i-1][t]

frac = float(input())
n = int(len(str(frac).split('.')[1]))
t = int(input())

print(max_grade('0.' + str(int(frac * 10)).zfill(n), n, t))
