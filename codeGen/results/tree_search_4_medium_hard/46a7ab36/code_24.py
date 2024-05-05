import sys

# Read input from stdin
t = int(input())

# Initialize modulo value
mod = 10**8 + 7

for _ in range(t):
    n, m = map(int, input().split())
    
    # Initialize dp array with size (n+1) * (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: only one way to form a word of length 0
    dp[0][0] = 1
    
    # Fill up the dp array based on the given rules
    for i in range(1, n + 1):
        if i < n / 2:
            for j in range(i):
                dp[i][j] = 0
        else:
            for j in range(i - m + 1):
                dp[i][j] = 0
        
        for j in range(min(i, m)):
            if i % 2 == 0 and j > 0:
                dp[i][j] += (n - (i // 2)) * dp[(i // 2) - 1][j - 1]
            else:
                dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= mod
    
    # Print the answer
    print(dp[-1][-1])
