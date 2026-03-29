n = int(input())
a, b, c = [int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()]

dp = [[0]*(n//2+1) for _ in range(n)]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], c[i-1])
    for j in range(1, min(i//2+1, n//2)+1):
        dp[i][j] = max(a[i-1]+dp[i-1][j-1], b[i-1]+dp[i-1][j], c[i-1]+dp[i-1][j+1])

print(dp[-1][-1])
