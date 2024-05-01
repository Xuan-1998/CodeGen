from sys import stdin

n, m = map(int, stdin.readline().split())

# Initialize dp array
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            k = min(i, j)
            for size in range(1, k + 1):
                if i >= size and j >= size:
                    dp[i][j] = min(dp[i][j], dp[i - size][j - size] + 1)

print(dp[n][m])
