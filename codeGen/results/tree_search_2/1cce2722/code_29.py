n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if a[i] != a[j]:
            dp[i][j] = min(dp[i-1][k] for k in range(j)) + 1
        else:
            dp[i][j] = dp[i-1][j]

print(min(dp[-1]))
