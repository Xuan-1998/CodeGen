python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        if A[j - 1] >= 1:
            dp[1][j] = 1
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            count = [0] * (N + 1)
            for k in range(1, N + 1):
                count[k] += dp[i - 1][k]
                if count[j] <= A[j - 1]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up all dp[N][j] for the final result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


