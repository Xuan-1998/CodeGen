n = int(input())
a = list(map(int, input().split()))
k = (max(a) + min(a)) // 2

dp = [[0] * (2*n-1) for _ in range(n)]

for i in range(n):
    dp[i][i] = a[i]
for i in range(1, n):
    for j in range(i*2-1, (n-1)*2+1):
        if i == 0:
            continue
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1]) + (a[i] == k or a[i] == k+1 or a[i] == k-1)

print(max(dp[n-1]))
