MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Create dp table and initialize
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Fill the dp table
    for i in range(2, N + 1):
        prefix_sum = [0] * (N + 1)
        for j in range(1, N + 1):
            prefix_sum[j] = (prefix_sum[j - 1] + dp[i - 1][j]) % MOD
        
        for j in range(1, N + 1):
            dp[i][j] = prefix_sum[N]
    
    # Calculate the final answer
    answer = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(answer)


