n = int(input())
marks = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(i+1):
        dp[i][k] = min(dp[i-1][j] + k*(n-j) for j in range(k+1))

print(min(dp[n]))
