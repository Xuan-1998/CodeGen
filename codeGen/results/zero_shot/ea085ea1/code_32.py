s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
