from sys import stdin

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j+1):
            if A[k-1] < A[k]:
                dp[i][j] = min(dp[i][j], dp[i][k-1] + 1)

print(dp[0][n-1])
