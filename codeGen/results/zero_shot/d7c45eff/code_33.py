code
k = int(input())
s = input().strip()
dp = [[0] * 2 for _ in range(k + 1)]

for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) if s[i - 1] <= s[i - 2] else dp[i - 1][1]

print(''.join(s[:k] if k == i and dp[i][0] > dp[i][1] else s[:i]))

