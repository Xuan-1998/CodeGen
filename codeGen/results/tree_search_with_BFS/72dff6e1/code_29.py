python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    # dp[i][j] represents the number of valid sequences of length i where the maximum element is j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: an empty sequence
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # We need to sum dp[i-1][k] for all k <= j
            # We use a prefix sum array to make this summation efficient
            prefix_sum = [0] * (N + 1)
            for k in range(1, N + 1):
                prefix_sum[k] = (prefix_sum[k-1] + dp[i-1][k]) % MOD
            
            # Now calculate dp[i][j]
            if A[j-1] >= i:
                dp[i][j] = prefix_sum[j]
    
    # The final answer is the sum of dp[N][j] for all 1 <= j <= N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)


