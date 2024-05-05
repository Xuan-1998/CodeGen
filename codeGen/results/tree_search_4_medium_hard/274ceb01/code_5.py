n = int(input())
marks = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if marks[j] < i:
            dp[i][j] = min(dp[i-1][k-1] + (i-k)*marks[i-1] + dp[k][j-1] - marks[j-1]
                          for k in range(j))
        else:
            dp[i][j] = 0

print(min(dp[n]))
