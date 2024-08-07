MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize dp for sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # DP transition
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if A[j-1] >= i and A[k-1] >= i:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)


