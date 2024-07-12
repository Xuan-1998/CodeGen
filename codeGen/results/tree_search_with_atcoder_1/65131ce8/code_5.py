MOD = 998244353

def count_good_vertices(N, d):
    # Initialize DP table
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case
    dp[1][0] = 1
    
    # Fill the DP table
    for i in range(2, N+1):
        for j in range(i):
            for k in range(1, i):
                for x in range(j+1):
                    if j - x >= 0 and dp[k][x] > 0 and dp[i-1-k][j-1-x] > 0:
                        dp[i][j] = (dp[i][j] + dp[k][x] * dp[i-1-k][j-1-x]) % MOD
    
    # Calculate the total number of good vertices
    total_good_vertices = 0
    for i in range(1, N+1):
        for j in range(N):
            if dp[i][j] > 0 and d[i-1] == j:
                total_good_vertices = (total_good_vertices + dp[i][j]) % MOD
    
    return total_good_vertices

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
d = list(map(int, data[1:]))

# Calculate and print the result
result = count_good_vertices(N, d)
print(result)

