def ways_to_sum(arr, N):
    MOD = 10**9 + 7

    dp = [[0] * (N+1) for _ in range(len(arr)+1)]
    dp[0] = [1] * (N+1)

    for i in range(1, len(arr)+1):
        for j in range(N+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-arr[i-1]]) % MOD

    return dp[-1][-1]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(ways_to_sum(arr, N))
