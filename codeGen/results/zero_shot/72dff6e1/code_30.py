def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        if A[j - 1] > 0:
            dp[1][j] = 1
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] >= i:
                dp[i][j] = sum(dp[i - 1][k] for k in range(1, N + 1) if A[k - 1] >= i - 1) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

