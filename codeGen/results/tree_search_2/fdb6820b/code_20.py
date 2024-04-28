def count_ways(array, N):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for k in array:
            if k <= N - i:
                dp[i] += dp[i - k]

    return dp[N] % (10**9 + 7)

# Read input from standard input
m, N = map(int, input().split())
array = list(map(int, input().split()))

print(count_ways(array, N))
