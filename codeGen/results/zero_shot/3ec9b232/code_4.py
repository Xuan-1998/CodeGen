n = int(input())
M = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1

for length in range(2, n+1):
    for i in range(length-1):
        for j in range(i+1, length):
            if M[i-1] < M[j-1]:
                dp[i][j] += dp[i-1][j-1]
            elif M[i-1] > M[j-1]:
                dp[i][j] = 0
            else:
                dp[i][j] += dp[i-1][j-1]

print(dp[n][n]%10**9+7)
