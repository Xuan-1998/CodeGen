def countOnes(n):
    k = len(str(n))
    dp = [[0] * (n+1) for _ in range(k)]
    
    # Initialize base case: single-digit numbers
    for i in range(10):
        dp[0][i] = 1 if i == 1 else 0
    
    # Fill up the dynamic programming table
    for i in range(1, k):
        for j in range(n+1):
            if j < 10**(i-1):
                dp[i][j] = 0
            elif j % 10 == 1:
                dp[i][j] = 1 + dp[i-1][int(j/10)]
            else:
                dp[i][j] = dp[i-1][int(j/10)]
    
    # Calculate the total count of digit 1
    total_count = 0
    for i in range(n+1):
        total_count += dp[k-1][i]
    
    return total_count

n = int(input())
print(countOnes(n))
