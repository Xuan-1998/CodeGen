from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [[False] * n for _ in range(n)]

for i in range(n):
    if i < arr[i]:
        dp[i][i-arr[i]] = True
    else:
        dp[i][i] = True

for i in range(1, n):
    for j in range(i):
        if dp[j][i-arr[i]]:
            dp[i][i] = True

print(dp[n-1][n-2])
