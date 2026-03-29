n = int(input())
m = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(min(i, n)):
        if m[i-1] == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += dp[i-1][j]

answer = sum(dp[n][i] for i in range(n+1)) % (10**9 + 7)
print(answer)
