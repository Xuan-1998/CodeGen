def can_partition(A):
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = {(i, j): False for i in range(N+1) for j in range(K+1)}
    
    dp[0][j] = True for 0 ≤ j < K
    For each i from 1 to N:
        For each k such that 0 ≤ k ≤ i and A[i-k+1:i+1] has at least K elements:
            if dp[i-k][j-1] is True and the absolute difference between A[i-k] and A[i] does not exceed M, then set dp[(i, k)] to True
    
    return dp[N][K]
