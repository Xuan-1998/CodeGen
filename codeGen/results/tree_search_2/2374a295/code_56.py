def count_good_sequences(n, k):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % k == 0:  # i is a multiple of k
            dp[i] = dp[(i // k) - 1]
        else:
            dp[i] = sum(dp[j] for j in range(i) if i % j == 0)
    return dp[n] % (10**9 + 7)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_good_sequences(n, k))
