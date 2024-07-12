MOD = 998244353

def count_good_trees(N, d):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if dp[k][j-1] > 0:
                    dp[i][j] += dp[k][j-1] * (d[i-1] - (i - k - 1))
                    dp[i][j] %= MOD
    
    # Sum up the results for all j
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

# Reading input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
d = list(map(int, data[1:]))

# Output the result
print(count_good_trees(N, d))

