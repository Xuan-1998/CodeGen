MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will represent the number of valid sequences of length i where the last element is j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: an empty sequence is valid
    dp[0][0] = 1
    
    # Prefix sum array to optimize the sum calculation
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
    prefix_sum[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Calculate dp[i][j] using the prefix sums
            dp[i][j] = prefix_sum[i-1][j]
            if i - A[j-1] - 1 >= 0:
                dp[i][j] -= prefix_sum[i - A[j-1] - 1][j]
            dp[i][j] = (dp[i][j] + MOD) % MOD
        
        # Update the prefix sum array
        for j in range(1, N + 1):
            prefix_sum[i][j] = (prefix_sum[i][j-1] + dp[i][j]) % MOD
    
    # Sum up all dp[N][j] for j from 1 to N
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

