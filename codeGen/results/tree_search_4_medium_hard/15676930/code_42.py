from sys import stdin

n = int(stdin.readline())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = int(stdin.readline())
    for j in range(1, i):
        if j == 0:
            dp[i][j] = b_i = int(stdin.readline())
        elif j == i - 1:
            dp[i][j] = c_i = int(stdin.readline())
        else:
            dp[i][j] = max(dp[i-1][min(j+1, i-1)] + b_i if j == 0
                            else c_i if j == i-1
                            else a_i)

print(max(dp[n]))
