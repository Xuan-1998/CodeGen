python
MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will be the number of ways to form a sequence of length i using exactly j occurrences of integer i
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(N + 1):
            # We need to sum up ways to form sequences of length i-1 with k occurrences of integer i-1
            for k in range(min(A[i - 1], j) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    
    # The answer is the sum of dp[N][j] for all j from 0 to N
    result = sum(dp[N][j] for j in range(N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

