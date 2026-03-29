def num_ways(n, m):
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(m, -1, -1):
            dp[j] += dp[j - 1]
    return dp[m]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(num_ways(N, M) % (10 ** 9 + 7))
