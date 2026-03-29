n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    dp[i][i-1] = max(a[i], b[i])

for length in range(2, n):
    for i in range(n - length):
        j = i + length
        if a[j]:
            dp[i][j] = max(dp[i][j-1] + a[j], dp[i+1][j-1] + c[j])
        else:
            dp[i][j] = max(dp[i][j-1] + b[j], dp[i+1][j-1] + c[j])

print(max(dp[0]))
