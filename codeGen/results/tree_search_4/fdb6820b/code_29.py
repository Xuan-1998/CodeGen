def count_ways():
    m, N = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        if i < m:
            dp[i] = 1
        else:
            for j in range(i):
                dp[i] += dp[j]
            dp[i] %= (10**9 + 7)
    print(dp[N])

if __name__ == "__main__":
    count_ways()
