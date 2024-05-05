python
def solve():
    n = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))
    
    # Initialize a 2D table to store the maximum joy for each subarray
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill up the table
    for i in range(1, n + 1):
        for j in range(1, min(i, n - i + 1)):
            if i % 2 == 0:
                dp[i][j] = max(dp[i-1][j-1] + a_values[j-1], 
                               dp[i-1][j+1] + a_values[j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + b_values[j-1], 
                               dp[i-1][j+1] + c_values[j])
    
    # The maximum total joy is stored in the bottom-right cell of the table
    return dp[n][n]
