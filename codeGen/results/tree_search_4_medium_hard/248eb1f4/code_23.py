import sys

T = int(input())

for _ in range(T):
    M, X = map(int, input().split())
    
    dp = [[0] * (X + 1) for _ in range(X + 1)]

    for i in range(1, X + 1):
        for j in range(i):
            if j < M - 1:
                dp[i][j] = (dp[i-1][j+1] + M - 1) % i
            else:
                dp[i][j] = (dp[i-1][j+1] + 1) % i

    winners = [None] * (X + 1)
    for i in range(X, 0, -1):
        winners[i] = dp[i][0]

    print(' '.join(map(str, winners[1:])))
