import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the base case: f(0, k) = 0 for all k >= 0
    for k in range(n + 1):
        dp[0][k] = 0
    
    for i in range(1, n + 1):
        for k in range(1, min(i ** 0.5, n) + 1):
            # Update dp[i][k] = min(dp[i][k], 1 + f(j, k - 1))
            for j in range(1, i):
                if j ** 2 <= i:
                    dp[i][k] = min(dp[i][k], 1 + dp[j][k - 1])
    
    # Return the answer: dp[n][?]
    return dp[n].index(min(dp[n]))

print(solve())
