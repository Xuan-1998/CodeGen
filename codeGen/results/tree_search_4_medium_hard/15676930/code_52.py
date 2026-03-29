n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i][0] = max(b[0], c[0])
    else:
        dp[i][0] = max(a[i-1], b[i-1])

for j in range(1, n+1):
    for i in range(j, n+1):
        if j == 1:
            dp[i][j] = max(c[i-1], a[i-1] + (c[i-2] if i > 1 else b[i-2]))
        else:
            dp[i][j] = max(dp[i-1][j-1], a[i-1] + (dp[i-2][j-1] if i > 1 and j > 0 else c[i-1]))

print(max(dp[n]))
