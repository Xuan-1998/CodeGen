n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(i, n):
        dp[i][j] = max(c[j-1] + c[j], a[i-1] + max(dp[i-1][j-1], dp[i-1][j]), c[j] + max(dp[i][j-2], dp[i][j-1]))
print(max(0, dp[0][n-1]))
