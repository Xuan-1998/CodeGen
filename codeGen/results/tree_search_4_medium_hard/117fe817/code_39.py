import sys

def solve(n):
    MOD = 10**9 + 7
    dp = [[0] * (32) for _ in range(31)]
    
    # Base case: no integers less than or equal to 0
    dp[0][0] = 1
    
    for i in range(1, n+1):
        ones = bin(i).count('1')
        dp[i][ones] += (dp[i-1].index(min(dp[i-1])) + 1) % MOD
        
    # Calculate the total count
    total_count = sum(val for row in dp for val in row)
    
    return int(total_count) % MOD

n = int(sys.stdin.readline())
print(solve(n))
