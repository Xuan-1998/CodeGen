import sys
A, B = map(int, input().split())
dp = [[False] * (B + 1) for _ in range(A + 1)]

for i in range(A + 1):
    for j in range(min(i, B) + 1):
        if i == 0:
            dp[i][j] = j <= B
        elif j == 0:
            dp[i][j] = i <= A
        else:
            dp[i][j] = dp[i-1][j-1] or dp[i-1][j+1]

for i in range(A + 1):
    for j in range(min(i, B) + 1):
        if dp[i][j]:
            X = i - (B - j)
            Y = j
            print(X, Y)
            sys.exit()

print(-1)
