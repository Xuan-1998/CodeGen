from sys import stdin

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [["" for _ in range(2)] for _ in range(n+1)]

for i in range(n+1):
    if i == 0:
        dp[i][0] = ""
        dp[i][1] = ""
    elif i == 1:
        dp[i][0] = s[0]
        dp[i][1] = s[0] + s[0]
    else:
        for j in range(2):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], s[i-1] + dp[i-1][1-j])
            elif j == 1:
                dp[i][j] = min(s[i-1] + dp[i-2][1-j], dp[i-1][1-j])

print(min(dp[k][0], dp[k][1]))
