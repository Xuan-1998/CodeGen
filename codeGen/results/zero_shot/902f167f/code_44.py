n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0] = [0] * (m + 1)
for i in range(1, n + 1):
    dp[i][0] = 1
min_squares = float('inf')
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= j:
            min_squares = min(min_squares, dp[i - j][j] + (n - i) // j)
print(min_squares)
