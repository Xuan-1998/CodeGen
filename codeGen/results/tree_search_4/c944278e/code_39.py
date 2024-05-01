import sys

def solve(n, s):
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    winners = {}
    
    # Base case: Initialize dp[0]
    for j in range(1 << n):
        dp[0][j] = bin(j).count('1') % 2 == 1
    
    # Transition from dp[i-1][k] to dp[i][j]
    for i in range(1, n + 1):
        for j in range(1 << n):
            if s[i - 1] ^ (j >> (n - i)) & 1:
                dp[i][j] = dp[i - 1][j >> 1]
            else:
                dp[i][j] = dp[i - 1][j] or j & 1
    
    # Store the winning teams for each prefix
    for i in range(1, n + 1):
        winners[s[:i]] = {j for j in range(1 << n) if dp[i][j]}
    
    # Find the intersection of all sets in dp_winners
    return set.intersection(*winners.values())

# Read input from stdin
n = int(input())
s = input().strip()

print(solve(n, s))
