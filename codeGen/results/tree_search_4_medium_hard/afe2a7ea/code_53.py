import sys

# Define the modulo value for calculation
mod = 998244353

def solve():
    # Read the input value N from stdin
    N = int(input())
    
    # Initialize the DP table with zeros, 
    # where dp[i][k] represents the minimum number of towers that can send signal to town k after building i towers.
    dp = [[0]*(N+1) for _ in range(N+1)]

    # Fill the DP table using your intuition
    for n in range(1, N+1):
        for k in range(min(n+1, N+1)):
            if k > 0:
                dp[n][k] = min(dp[n-1][k-1] + (n == k) or 0, 
                               dp[n-1][k])
    
    # Calculate the total number of possibilities
    total_possibilities = sum(2**i for i in range(N+1))
    
    # The answer is the sum of all possible cases where there's at least one tower that doesn't send signal to town 0
    answer = sum(dp[n][k] for n in range(N+1) for k in range(min(n+1, N+1)) if k > 0)
    
    # Return the result modulo the given value
    return (answer * total_possibilities ** (N+1 - 2)) % mod

print(solve())
