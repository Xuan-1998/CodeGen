import sys

dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
for i in range(A + 1):
    dp[i][0] = 0
for i in range(B + 1):
    dp[0][i] = float('inf')
for i in range(1, A + 1):
    for j in range(1, B + 1):
        if i <= j:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = dp[i - j][j]
x, y = float('inf'), float('inf')
for X in range(A + 1):
    for Y in range(B + 1):
        if A == X + Y and B == X ^ Y:
            x, y = min(X, Y), max(X, Y)
            break
if x > y:
    print(f"{x} {y}")
else:
    print(-1)
