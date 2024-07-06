def count_valid_sequences(N, A):
    MOD = 998244353
    
    # dp[i][j] will store the number of valid sequences of length i ending with j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initial condition: there's one way to have a sequence of length 0 (the empty sequence)
    dp[0][0] = 1
    
    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] > 0:
                for k in range(1, N + 1):
                    if dp[i - 1][k] > 0 and A[k - 1] > 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

