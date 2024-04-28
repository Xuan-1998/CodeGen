n = int(input())
str1 = input()
str2 = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if i == j and dp[i][j] > ans:
            ans = dp[i][j]

print(ans)
