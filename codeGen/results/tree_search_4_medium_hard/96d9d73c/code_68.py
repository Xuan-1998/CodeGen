import sys
from collections import defaultdict

def can_partition(A):
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    
    dp = [[False] * (K + 1) for _ in range(N + 1)]
    valid = False
    
    for k in range(1, K + 1):
        if k == 1 or max(A[:k]) - min(A[:k]) <= M:
            dp[0][k] = True
        else:
            dp[0][k] = False
        
        for i in range(N):
            for j in range(k, 0, -1):
                if (i == 0 or dp[i-1][j-1]):
                    if max(A[i-k+1:i+1]) - min(A[i-k+1:i+1]) <= M:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                break
    
    valid = any(dp[N-1][k] for k in range(K, 0, -1))
    
    print(valid)

can_partition(input().split())
