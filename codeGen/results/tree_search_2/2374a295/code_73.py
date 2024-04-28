def count_good_sequences(n, k):
    MOD = 10000000007

    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(2, n + 1):
        for j in range(min(i, k), -1, -1):
            if j % i == 0:
                dp[j] += dp[(j // i)]
            dp[j] %= MOD

    return dp[k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
