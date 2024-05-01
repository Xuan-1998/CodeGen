import sys
from collections import defaultdict

def solve(m, N, arr):
    MOD = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(N + 1)]
    
    # Initialize base cases
    dp[0][0] = 1
    
    # Fill up the table using a bottom-up approach
    arr.sort()
    for i in range(1, N + 1):
        for j in range(m, -1, -1):
            if j > 0 and arr[j-1] <= i:
                dp[i][j] = (dp[i-arr[j-1]][j-1] + dp[i][j]) % MOD
    return dp[N][m]

# Read input from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(m, N, arr))
