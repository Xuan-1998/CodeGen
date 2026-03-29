def findXY():
    A, B = map(int, input().split())
    
    # Initialize dp table with zeros
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    
    dp[0][0] = 0
    
    for i in range(1, A + 1):
        for j in range(min(i, B) + 1):
            if i >= j:
                X = i - j
                Y = X ^ j
                
                # Update dp[i][j] with the minimum value of Y
                dp[i][j] = min(dp[i][j], Y)
    
    if dp[A][B] == float('inf'):
        print(-1)
    else:
        X, Y = A - dp[A][B], dp[A][B]
        print(X, Y)

findXY()
