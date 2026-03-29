def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Transition
    for i in range(2, N + 1):
        # Prefix sums to optimize the summation
        prefix_sum = [0] * (N + 1)
        for k in range(1, N + 1):
            prefix_sum[k] = (prefix_sum[k-1] + dp[i-1][k]) % MOD
        
        for j in range(1, N + 1):
            if A[j-1] >= i:
                dp[i][j] = prefix_sum[N]
            else:
                dp[i][j] = (prefix_sum[N] - prefix_sum[A[j-1]]) % MOD
    
    # Sum up all dp[N][j] for j from 1 to N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)


