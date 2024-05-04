import sys

# Define the modulo value
MOD = 998244353

def count_blocks(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(10):
        dp[1][i+1] = 1
    
    # Fill up the dynamic programming table
    for len_ in range(2, n + 1):
        for digit in range(10):
            for i in range(len_ - 1):
                if (digit == 0) or ((len_ > 1) and (i > 0)):
                    dp[len_][digit*10**(len_-1)+i] += dp[i][digit]
    
    # Initialize the result array
    res = [0] * (n + 1)
    
    # Fill up the result array
    for i in range(1, n + 1):
        for j in range(10):
            if i >= len_:
                res[i] += dp[len_][j*10**(len_-1)] % MOD
            else:
                res[i] += (dp[i][j] * pow(10, len_ - i, MOD)) % MOD
    
    return [x % MOD for x in res]

# Read the input from stdin
n = int(input())

# Calculate and print the result
print(*count_blocks(n), sep=' ')
