import sys

n, k, z = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (k+1) for _ in range(n)]

for i in range(1, n):
    dp[i][0] = arr[i]
for i in range(1, n):
    for j in range(min(i-1, z)+1, min(k+1, i+1)):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + arr[i]

print(max(dp[n-1]))
