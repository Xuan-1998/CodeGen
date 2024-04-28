from collections import defaultdict

N = int(input())
str1 = input()
str2 = input()

dp = [[0] * (N + 1) for _ in range(N + 1)]
ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])

print(ans)
