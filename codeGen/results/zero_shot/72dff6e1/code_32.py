python
MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will store the number of valid sequences of length i with highest number j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There is one way to have a sequence of length 0
    for j in range(N + 1):
        dp[0][j] = 1

    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j-1]
            if A[j-1] >= i:
                dp[i][j] += dp[i-1][j]
            dp[i][j] %= MOD

    # The answer is the sum of all dp[N][j] for 1 <= j <= N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

