import sys

def winner_game(M, X):
    dp = [[0] * (X + 1) for _ in range(X + 1)]
    for i in range(1, X + 1):
        dp[i][i] = i
    for length in range(2, X + 1):
        for i in range(length - 1, X + 1):
            if length == 2:
                dp[i][length] = min(range(1, i + 1), key=lambda k: (k * ((i + M - 2)) % X) + dp[k-1][(i+M-2)%X])
            else:
                for k in range(1, i + 1):
                    if (k * ((i + M - 2)) % X) + dp[i-k][((i+M-2))%X] < (k * ((length + M - 2)) % X) + dp[k-1][(length+M-2)%X]:
                        dp[i][length] = k
                        break
    return [dp[i][j] for i in range(X, 0, -1) for j in range(1, X + 1)]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*winner_game(M, X))
