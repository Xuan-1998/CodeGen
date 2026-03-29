from collections import defaultdict

def min_operations():
    N = int(input())
    A = list(map(int, input().split()))
    
    # Initialize dp table with default value as infinity
    dp = defaultdict(lambda: [float('inf')] * (max(A) + 1))
    
    # Base cases for dp[0][j] and handle edge case where j is greater than A[i]
    for j in range(max(A) + 1):
        if j < A[0]:
            dp[0][j] = 0
        else:
            dp[0][j] = float('inf')
    
    # Fill up the dp table using bottom-up dynamic programming and memoization
    for i in range(1, N):
        for j in range(max(A) + 1):
            if j < A[i]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][k] + (A[i-1] > k) for k in range(j+1)) if i > 0 else float('inf')
    
    # Return the minimum number of operations needed to make the array strictly increasing from the start
    return dp[N-1][-1]

print(min_operations())
