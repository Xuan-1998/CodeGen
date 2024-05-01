import sys

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        if a[i] == a[j]:
            dp[i][j] = dp[i+1][j-1] + 3
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])

print(max(min(row) for row in dp))
