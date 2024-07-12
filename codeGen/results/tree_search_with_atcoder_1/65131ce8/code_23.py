python
MOD = 998244353

def count_good_vertices(N, d):
    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(d[i - 1] + 1):
                if i - 1 - k >= 0:
                    dp[i][j] += dp[i - 1][j - 1] * dp[i - 1 - k][j - 1]
                    dp[i][j] %= MOD
    
    # Sum up the dp[N][j] values for all j (from 1 to N)
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
d = list(map(int, data[1:]))

# Get the result
result = count_good_vertices(N, d)

# Print the result
print(result)

