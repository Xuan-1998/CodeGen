python
MOD = 998244353

def count_good_vertices(N, d):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base cases
    dp[1][1] = 1
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(d[i - 1] + 1):
                if i - 1 - k >= 0:
                    dp[i][j] += dp[i - 1 - k][j - 1]
                    dp[i][j] %= MOD
    
    # Sum up the number of good vertices for all valid trees
    result = 0
    for i in range(1, N + 1):
        result += dp[N][i]
        result %= MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
d = list(map(int, data[1:]))

# Compute and print the result
print(count_good_vertices(N, d))

