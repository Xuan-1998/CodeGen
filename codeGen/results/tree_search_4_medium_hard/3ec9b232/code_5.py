import sys

def mergeWays(M):
    MOD = 10**9 + 7
    N = len(M)
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize base case: merging an empty array into itself is always possible.
    dp[0][0] = 1
    
    for i in range(1, N):
        for j in range(i+1):
            for k in range(j+1):
                dp[i][j] += dp[k][min(j,k)] * dp[N-1-k-1][min(N-j-1, N-1-k-1)]
                dp[i][j] %= MOD
    
    return dp[-1][-1]

# Read input
N = int(input())
M = list(map(int, input().split()))

print(mergeWays(M))
