import sys
MOD = 998244353

def solve():
    n = int(sys.stdin.readline())
    
    # Initialize dp array with zeros.
    dp = [0] * (n + 1)
    
    # Base case: If we have no towns, then there is only one way to set signal powers which is not setting any signal power. So the probability is 1.
    dp[0] = 1
    
    for i in range(1, n + 1):
        # Calculate the total number of ways to set signal powers for current town (i).
        total_ways = 2 ** (n - i)  # There are 2^(n-i) ways to choose which tower will be used.
        
        dp[i] = (dp[i - 1] * total_ways) % MOD
    
    return dp[-1]

print(solve())
