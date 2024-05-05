def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    prev_index = [None] * (n + 1)

    # Base case: no moves
    for i in range(1, n + 1):
        dp[i][0] = arr[i - 1]

    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j < z or prev_index[i] is None:
                # Try moving to the left (if allowed)
                dp[i][j] = max(dp[i - 1][j - 1] + arr[i - 2], dp[i - 1][j])
            else:
                # Can't move to the left, so try moving to the right
                dp[i][j] = dp[i - 1][j - 1] + arr[i - 1]

    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
