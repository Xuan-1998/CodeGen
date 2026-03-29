def find_winner(M, X):
    MOD = 10**9 + 7

    dp = [[-1]*X for _ in range(X+1)]

    def winner(i, j):
        if i <= 0 or j < 0:
            return -1
        if dp[i][j] != -1:
            return dp[i][j]
        
        if j == 0:
            return (i-1) % X

        winner_idx = (winner(i-1, j-1) + M - 1) % X
        dp[i][j] = winner_idx
        return winner_idx

    winners = []
    for i in range(1, X+1):
        winners.append(winner(X-i+1, X-i))

    return winners[::-1]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*find_winner(M, X))
