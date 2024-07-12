python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        if A[j - 1] >= 1:
            dp[1][j] = 1
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i - 1][k] > 0 and A[j - 1] >= i:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up the results for sequences of length N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


