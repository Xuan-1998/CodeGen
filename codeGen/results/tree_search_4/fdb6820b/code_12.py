def count_ways_to_form_N(array, N):
    MOD = 10**9 + 7

    n = len(array)
    dp = [[0] * (N+1) for _ in range(n+1)]

    # Base case: when N is 0, there's only one way to form it
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(N+1):
            if j >= array[i-1]:
                dp[i][j] = (dp[i-1][j-array[i-1]] + 1) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][N]

m, N = map(int, input().split())
array = list(map(int, input().split()))
print(count_ways_to_form_N(array, N))
