MOD = 998244353

def solve(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: A 1x1 matrix can either be [0] or [1]
    dp[1][1] = 2
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    
    # The answer is the number of valid NxM matrices
    print(dp[N][M])

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

solve(N, M)

