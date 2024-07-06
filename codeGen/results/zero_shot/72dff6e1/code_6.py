def count_valid_sequences(N, A):
    MOD = 998244353
    
    # dp[i][j] will store the number of valid sequences of length i with j elements used
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initial state: there's one way to have a sequence of length 0
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]  # Carry over the previous count
            if j > 0 and j <= A[i - 1]:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= MOD
    
    # Sum up all sequences of length N
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

