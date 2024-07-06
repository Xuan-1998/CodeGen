python
MOD = 998244353

def count_valid_sequences(N, A):
    # DP table where dp[i][j] is the number of valid sequences of length i ending with j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there's one way to have a sequence of length 0
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Count the number of valid sequences of length i ending with j
            for k in range(1, N + 1):
                if dp[i - 1][k] > 0 and dp[i - 1][k] + 1 <= A[k - 1]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

