n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = c[i-1]
    for j in range(1, min(i+1, n)+1):
        if i-j < 2:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+a[i-j])

print(max(dp[n]))
