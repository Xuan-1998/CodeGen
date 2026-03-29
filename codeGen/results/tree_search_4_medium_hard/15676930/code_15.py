from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 0
    dp[i][1] = 0 if i == 1 else b[0]
    for j in range(2, i+1):
        dp[i][j] = max(dp[i-1][0] + c[i-1],
                        dp[i-1][1] + b[i-1] if i % 2 == 0 else b[i-1],
                        dp[i-2][0] + a[i-2])

print(max(dp[n]))
