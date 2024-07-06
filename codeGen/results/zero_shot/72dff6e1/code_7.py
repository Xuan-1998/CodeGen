def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # There's one way to form a sequence of length 0
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1]  # Carry forward the previous count
            if i >= j and A[j - 1] >= i:
                dp[i][j] += dp[i - j][j]
                dp[i][j] %= MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:1 + N]))
    
    print(count_valid_sequences(N, A))

