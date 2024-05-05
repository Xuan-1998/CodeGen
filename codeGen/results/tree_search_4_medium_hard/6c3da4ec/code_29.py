from collections import defaultdict

n = int(input())
s = input()

dp = [[0] * n for _ in range(n)]
prefix_sum = defaultdict(int)

for i in range(n):
    prefix_sum[i] = 0
    if s[i] == '1':
        prefix_sum[i] += 1

max_or = 0

for i in range(1, n):
    dp[i][i] = int(s[i]) - (prefix_sum[i-1] << 1)
    max_or = max(max_or, dp[i][i])

for l in range(2, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        if i > 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) | (prefix_sum[j] << l)
            max_or = max(max_or, dp[i][j])
        else:
            dp[i][j] = int(s[:l]) - ((prefix_sum[l-1] << l) & ~int('1' * l, 2))
            max_or = max(max_or, dp[i][j])

print(bin(max_or)[2:].zfill(n).lstrip('0'))
