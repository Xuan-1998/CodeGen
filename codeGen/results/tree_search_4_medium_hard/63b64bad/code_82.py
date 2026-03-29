def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    
    # Initialize dp array with dimensions (n+1) x (10^9 + 1)
    dp = [[-1] * (10**9 + 1) for _ in range(n+1)]
    
    # Base case: initialize dp[0][a] to 0
    for a in seq:
        dp[0][a] = 0
    
    # Fill in the dynamic programming table
    for x in range(2, n+1):
        for y in range(x-1):
            if x > n or y <= 0:
                dp[y][seq[x-1]] = -1
            else:
                dp[y][seq[x-1]] = max(dp[y+seq[x-1]][seq[x-1]], 
                                        dp[max(0, y-seq[x-1]))[seq[x-1]]
    
    # Return the final value of y for the given sequence
    return dp[n-1][seq[-1]]

print(solve())
