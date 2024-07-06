python
def count_valid_sequences(N, A):
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= A[j - 1]:
                dp[i][j] += dp[i - A[j - 1]][j - 1]
            dp[i][j] %= MOD

    result = 0
    for j in range(1, N + 1):
        result += dp[N][j]
        result %= MOD

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N + 1]))
    print(count_valid_sequences(N, A))

