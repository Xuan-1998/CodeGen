def winner(M, X):
    MOD = 10**9 + 7
    dp = [[0] * (X+1) for _ in range(X+1)]
    
    # Base case: For M=1, the last person standing is always the first one.
    for i in range(1, X+1):
        dp[i][0] = i-1
    
    # Memoize intermediate results
    memo = {}
    
    def helper(i, j):
        if (i, j) not in memo:
            if j == 0:
                result = j
            elif (j+i-2)%M == 0:
                result = (j+1)%i
            else:
                result = helper((j+i-2)//M, (j+i-2)%M)
            
            # Store the result in memo for future lookups.
            memo[(i, j)] = result
            
        return memo[(i, j)]
    
    for i in range(X+1):
        if dp[i][0] == -1:
            break
        print(dp[i][0], end=' ')
    print()
