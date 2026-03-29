from sys import stdin, maxsize

n = int(stdin.readline())
b = [int(stdin.readline()) for _ in range(n)]

dp = [[maxsize] * (1000001) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 1000001):
        if j <= b[i-1]:
            dp[i][j] = min(dp[k][min(b_k, j)] + (i-k) for k in range(i))
        else:
            dp[i][j] = dp[i-1][j]
print(min(dp[n]))
