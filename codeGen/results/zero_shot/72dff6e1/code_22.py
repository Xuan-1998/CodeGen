MOD = 998244353

def count_valid_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: an empty sequence is trivially valid
    for j in range(N + 1):
        dp[0][j] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1]  # Start with the value from the previous j
            if i - 1 >= A[j - 1]:
                dp[i][j] -= dp[i - 1 - A[j - 1]][j - 1]
            dp[i][j] += dp[i - 1][j]
            dp[i][j] %= MOD
    
    return dp[N][N]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    result = count_valid_sequences(N, A)
    print(result)

