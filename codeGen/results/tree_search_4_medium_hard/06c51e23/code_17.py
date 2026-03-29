def max_grade(n, t):
    dp = [0] * (n + 1)
    
    # Initialize base case
    dp[0] = 0
    
    for i in range(1, n + 1):
        round_value = int(str(t).zfill(i)[::-1].replace('9', '8') + '9', 10) - 1
        dp[i] = max(dp[i-1], round_value + dp[i-1 - (i - round_value)])
    
    return dp[n]

# Example usage:
n, t = map(int, input().split())
print(max_grade(n, t))
