MOD = 998244353

def count_good_vertices(N, d):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case

    for i in range(1, N + 1):
        for j in range(0, i + 1):
            for k in range(i):
                dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k - 1][0]) % MOD
                dp[i][j] = (dp[i][j] + dp[k][j] * dp[i - k - 1][j]) % MOD

    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i]) % MOD

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))

    print(count_good_vertices(N, d))

