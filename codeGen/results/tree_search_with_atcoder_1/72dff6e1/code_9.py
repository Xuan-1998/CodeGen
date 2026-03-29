MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    # DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # We need to check if we can place j at position i
            valid = True
            count = [0] * (N + 1)
            for k in range(1, i):
                count[dp[k][j]] += 1
                if count[dp[k][j]] > A[dp[k][j] - 1]:
                    valid = False
                    break
            if valid:
                dp[i][j] = sum(dp[i-1][k] for k in range(1, N + 1)) % MOD
    
    # Summing up the valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


