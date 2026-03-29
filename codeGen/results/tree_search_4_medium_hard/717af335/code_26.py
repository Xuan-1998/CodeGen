import sys

A = int(input())
B = int(input())

dp = [[False] * (B + 1) for _ in range(A + 1)]

for i in range(A + 1):
    for j in range(B + 1):
        if i == 0 or j == 0:
            dp[i][j] = True
        else:
            if i > 0 and (A - i) ^ (B - j) <= A - i:
                dp[i][j] = dp[i - 1][j]
            elif j > 0 and (A - i) ^ j <= B - j:
                dp[i][j] = dp[i][j - 1]

X, Y = 0, B
for i in range(A + 1):
    for j in range(B + 1):
        if dp[i][j]:
            X, Y = i, j
            break

if (A != X + Y) or (B != X ^ Y):
    print(-1)
else:
    print(X, ' ', Y)
