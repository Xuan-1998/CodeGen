python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize base case
    for j in range(1, N+1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if i <= A[j-1] and i <= A[k-1]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Compute the final answer
    result = sum(dp[N][j] for j in range(1, N+1)) % MOD
    
    print(result)


