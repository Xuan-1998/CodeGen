python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize dp[0][j] = 1 for all j from 1 to N
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Calculate prefix_sum for dp[0]
    for j in range(1, N + 1):
        prefix_sum[0][j] = prefix_sum[0][j - 1] + dp[0][j]
    
    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] >= i:
                dp[i][j] = (prefix_sum[i - 1][N] - prefix_sum[i - 1][j - 1]) % MOD
            else:
                dp[i][j] = 0
        
        # Update prefix_sum for current i
        for j in range(1, N + 1):
            prefix_sum[i][j] = (prefix_sum[i][j - 1] + dp[i][j]) % MOD
    
    # Calculate the final answer
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


