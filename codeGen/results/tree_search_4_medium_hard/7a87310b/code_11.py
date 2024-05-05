def count_matrices():
    T = int(input())
    dp = [[0] * (2501) for _ in range(2501)]
    
    # Base case initialization
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][i] = 2  # Invertible matrices with trace i and determinant i
        if i > 1:
            dp[i][0] = dp[i-1][0] + (dp[i-1][i-1] * 2)  # Invertible matrices with trace i and determinant 0
    
    for t in range(1, N+1):
        for j in range(t-1, -1, -1):
            if j > 0:
                dp[t][j] += dp[j][j-j] + dp[t-j][j]
    
    # Calculate the sum of counts for all possible trace values from 1 to N where the determinant is positive
    total_count = sum(dp[i][i] for i in range(1, N+1) if i <= j)
    
    return total_count

print(count_matrices())
