import sys

def can_partition(A, K, M):
    N = len(A)
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]
    
    # Base case: When the number of elements is less than K, it's always possible to partition them into at most K partitions.
    for i in range(N+1):
        if i < K:
            dp[i][K] = True
        else:
            dp[i][K] = False
    
    # Fill up the dp table based on your intuition
    for i in range(1, N+1):
        for j in range(min(i, K), 0, -1):
            if max(A[:i]) - min(A[:i]) <= M:
                if j == 1 or (j > 1 and dp[i-1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                dp[i][j] = False
    
    return dp[N][K]

# Read input from stdin
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Print the answer to stdout
print(can_partition(A, K, M))
