code
k = int(input())
n = int(input())
s = input()

dp = [["" for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = ""

for j in range(1, min(k+1, n+1)):
    if s[j-1] == s[-1]:
        dp[n][j] = dp[n][j-1]
    else:
        dp[n][j] = dp[n-1][j]

for i in range(n-1, -1, -1):
    for j in range(min(k+1, n-i), 0, -1):
        if s[i] == s[-1]:
            dp[i][j] = min(dp[i][j-1], dp[i+1][j])
        else:
            dp[i][j] = min(dp[i][j-1], dp[i+1][j])

for j in range(k, -1, -1):
    print(dp[0][j], end="")
