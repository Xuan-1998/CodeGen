def find_winner(M, X):
    dp = [[0]*(M) for _ in range(X+1)]
    
    for i in range(1, X+1):
        for j in range(M):
            if j == M-1:
                dp[i][j] = (j+1)%i
            else:
                winner = (dp[i-1][(j+M-2)%i]+1)%i
                dp[i][j] = winner
    
    return [dp[x][0] for x in range(1, X+1)]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*find_winner(M, X))
