n = int(input())
str1 = input()
str2 = input()

dp = [[0] * (n+1) for _ in range(n+1)]
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if str1[i:j] in str2:
            dp[i][j] = max(dp[i][j], dp[i][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans)
