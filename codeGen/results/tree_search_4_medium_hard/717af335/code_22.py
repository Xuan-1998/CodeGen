import sys

A, B = map(int, input().split())
dp = [[False] * (B+1) for _ in range(A+1)]

for i in range(A+1):
    dp[i][0] = True
    if i > 0:
        dp[i][0] = (dp[i-1][0] and A == i)
for j in range(B+1):
    dp[0][j] = True
    if j > 0:
        dp[0][j] = (dp[0][j-1] and B == j)

for i in range(1, A+1):
    for j in range(1, min(A, B)+1):
        if dp[i-1][j]:
            X = i-1
            Y = j-(i-1)
            print(f"{X} {Y}")
            sys.exit()
        elif dp[i-1][j-1]:
            X = i-1
            Y = j-i
            print(f"{X} {Y}")
            sys.exit()

print(-1)
