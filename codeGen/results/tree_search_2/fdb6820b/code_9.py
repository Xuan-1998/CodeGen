import sys

def count_ways(m, N, arr):
    MOD = 10**9 + 7
    
    # Initialize the dp table with zeros
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to form a sum of 0 is to not include any numbers

    for n in range(1, N + 1):
        for num in arr:
            if n >= num:
                dp[n] += dp[n - num]
                dp[n] %= MOD

    return dp[N]

# Read input from stdin
m = int(input())
N = int(input())
arr = list(map(int, input().split()))

# Compute and print the result
ways = count_ways(m, N, arr)
print(ways)
