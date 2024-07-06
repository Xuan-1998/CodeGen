python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # dp[i][j][k] - number of valid sequences of length i with last element j and k occurrences of j
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Base case: dp[0][0][0] = 1
    dp[0][0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, A[j-1] + 1):
                for l in range(1, N + 1):
                    if l != j:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][l][k]) % MOD
                    elif k > 1:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
    
    result = 0
    for j in range(1, N + 1):
        for k in range(1, A[j-1] + 1):
            result = (result + dp[N][j][k]) % MOD
    
    print(result)


