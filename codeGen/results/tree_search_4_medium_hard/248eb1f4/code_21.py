def winners(X, M):
    dp = [[0] * (M) for _ in range(X+1)]
    
    # Base case: when there are no coins, player 1 always wins
    for i in range(1, X+1):
        dp[i][0] = 1
    
    for i in range(1, X+1):
        for j in range(1, M-1):
            if (i - 1) % X == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[(i - 1) % X][j-1]
        
        for j in range(M-1, i):
            dp[i][j] = dp[(i - (j + 1)) % X][M-2]
    
    return [dp[x][M-1] for x in range(1, X+1)]

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    print(*winners(X, M))
