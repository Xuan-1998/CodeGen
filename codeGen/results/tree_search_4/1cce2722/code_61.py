import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * 106 for _ in range(n + 1)]
hash_map = {}

for i in range(1, n + 1):
    hash_map[a[i - 1]] = i
    dp[i][0] = 1

for i in range(1, n + 1):
    for k in range(1, min(i + 1, 106)):
        if a[i - 1] == k:
            for j in range(k - 2, k + 3):
                if j != k and j in hash_map:
                    dp[i][k] = max(dp[i][k], dp[hash_map[j]][j])
        else:
            dp[i][k] = dp[i - 1][k]

print(max(dp[n]))
