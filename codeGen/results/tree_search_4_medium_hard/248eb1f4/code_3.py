import sys

def coin_game(M, X):
    dp = [[0] * (X + 1) for _ in range(X + 1)]

    for i in range(1, X + 1):
        for j in range(i, X + 1):
            if j < M:
                dp[i][j] = j
            else:
                min_winner = sys.maxsize
                for k in range(j - M + 1, j):
                    winner = dp[i - 1][k]
                    if winner < min_winner:
                        min_winner = winner
                dp[i][j] = min_winner + 1

    return [dp[i][X] for i in range(1, X + 1)]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*coin_game(M, X))
