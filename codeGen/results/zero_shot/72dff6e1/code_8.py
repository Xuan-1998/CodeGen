def count_valid_sequences(N, A):
    MOD = 998244353
    
    # dp[i][j] will store the number of valid sequences of length i with the last element being j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: one way to have an empty sequence
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i-1][k] > 0 and A[j-1] > 0:  # Check if adding j to the sequence is valid
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # The result is the sum of all dp[N][j] for j from 1 to N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

