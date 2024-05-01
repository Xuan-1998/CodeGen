code
n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    dp[i][0] = max(arr[:i+1])
for j in range(1, k+1):
    for i in range(j-1, n):
        dp[i][j] = max(dp[i-j][j-1], arr[i-j+1:i+1].max()) + dp[i-j][j]
print(dp[-1][-1])
