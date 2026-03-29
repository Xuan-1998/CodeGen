MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # dp[i][j][k] means the number of valid sequences of length i ending with element j having k occurrences of j
    dp = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Initialization
    for j in range(1, N + 1):
        dp[1][j][1] = 1
    
    # Transition
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, A[j-1] + 1):
                for p in range(1, N + 1):
                    for c in range(1, A[p-1] + 1):
                        if p == j and k == c + 1:
                            dp[i][j][k] += dp[i-1][p][c]
                        elif p != j:
                            dp[i][j][k] += dp[i-1][p][c]
                        dp[i][j][k] %= MOD
    
    # Final Calculation
    result = 0
    for j in range(1, N + 1):
        for k in range(1, A[j-1] + 1):
            result += dp[N][j][k]
            result %= MOD
    
    print(result)


