def min_perfect_squares(n):
    # Initialize dp array with n+1 elements, all set to infinity
    dp = [float('inf')] * (n + 1)
    
    # Base case: 0 can be represented as 0 perfect squares
    dp[0] = 0
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    
    return dp[n]

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    print(min_perfect_squares(n))
