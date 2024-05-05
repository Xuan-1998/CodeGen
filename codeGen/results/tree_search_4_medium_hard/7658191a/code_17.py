def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the base case
    for i in range(1, n + 1):
        dp[i][0] = sum(arr[:i])

    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j <= z:
                max_score = max(dp[i - 1][j - 1] + arr[i], dp[i - 1][j] + arr[i])
            else:
                max_score = max(dp[i - 1][j - 1] + arr[i], dp[i - 1][z] + arr[i])
            dp[i][j] = max_score

    return dp[n][k]


t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
